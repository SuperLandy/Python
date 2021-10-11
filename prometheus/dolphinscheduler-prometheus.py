import pymysql
import prometheus_client
from flask import Flask, Response

app = Flask(__name__)


class Mysql:
    def __init__(self, host, user, pwd, database, sql):
        self.host = host
        self.user = user
        self.sql = sql
        self.pwd = pwd
        self.database = database

    def connect(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.database)
        self.curs = self.db.cursor(pymysql.cursors.DictCursor)

    def close(self):
        self.curs.close()
        self.db.close()

    def find(self):
        self.connect()

        try:
            self.curs.execute(self.sql)
            fc = self.curs.fetchall()
            return fc
        except pymysql.Error as error:
            print('runtime error :', error)
        finally:
            self.close()


def job_status():
    job_sql = """SELECT t1.name,t2.release_state
          from t_ds_process_definition t1
          LEFT JOIN t_ds_schedules t2
          ON t1.id = t2.id;"""
    job_result = Mysql('10.1.1.1', 'admin', 'admin', 'dolphinscheduler', job_sql).find()
    for job_metric in job_result:
        job_state.labels(job_metric['name']).set(job_metric['release_state'])


def master_status():
    master_sql = '''select instance_name from qrtz_scheduler_state'''
    master_result = Mysql('10.1.1.1', 'admin', 'admin', 'dolphinscheduler', master_sql).find()
    for master_metric in master_result:
        master_state.labels(master_metric['instance_name']).set(1)


@app.route('/metric', methods=['POST', 'GET'])
def metric():
    job_status()
    master_status()
    return Response(prometheus_client.generate_latest(registry), mimetype='text/plain')


@app.route('/', methods=['GET'])
def hello():
    return 'Hello word'


if __name__ == '__main__':
    # 获取job定时任务在线状态、master在线状态
    registry = prometheus_client.CollectorRegistry()
    job_state = prometheus_client.Gauge('ds_job_name', 'dolphinscheduler cron job status ', ['job_name'],
                                        registry=registry)
    master_state = prometheus_client.Gauge('ds_master_node', 'dolphinscheduler master node status ', ['instance_name'],
                                           registry=registry)
    app.run(host='127.0.0.1', port=5000)
