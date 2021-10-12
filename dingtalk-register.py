import redis
import time
import demjson
from dingtalk.crypto import DingTalkCrypto
from flask import request, Flask, jsonify
from dingtalk.storage.kvstorage import KvStorage
from dingtalk import AppKeyClient

app = Flask(__name__)


@app.route('/register', methods=['POST', 'GET'])
def register_sjj():
    # 需要注册事件名，全部注册
    register_callback = ding_client.callback.register_call_back(
        call_back_tags=['user_add_org', 'user_modify_org', 'user_leave_org', 'user_active_org',
                        'org_admin_add', 'org_admin_remove', 'org_dept_create', 'org_dept_modify',
                        'org_dept_remove', 'org_change', 'org_remove',
                        'label_user_change', 'label_conf_add', 'label_conf_modify', 'label_conf_del',
                        'edu_user_insert', 'edu_user_update', 'edu_user_delete',
                        'edu_user_relation_insert', 'edu_user_relation_update', 'edu_user_relation_delete',
                        'edu_dept_insert', 'edu_dept_update', 'edu_dept_delete',
                        'chat_add_member', 'chat_remove_member', 'chat_quit', 'chat_update_owner', 'chat_update_title',
                        'chat_disband',
                        'check_in', 'bpms_task_change', 'bpms_instance_change',
                        'attendance_check_record', 'attendance_schedule_change', 'attendance_overtime_duration',
                        'meetingroom_book', 'meetingroom_room_info'],
        token=token,
        aes_key=aes_key,
        url='http://128.14.229.133/callback'
    )
    app.logger.info('ding_talk register status: ', register_callback)


@app.route('/callback', methods=['POST'])
def ding_callback():
    pt = DingTalkCrypto(
        token=token,
        encoding_aes_key=aes_key,
        corpid_or_suitekey=corp_id
    )
    po = request.json["encrypt"]
    data = request.values
    app.logger.info('ding_talk request data: ', data)

    result = pt.encrypt_message(
        msg="success",
        nonce=data["nonce"],
        timestamp=int(time.time())
    )
    # 获取到事件及其他信息
    callback = pt.decrypt_encrypt_str(
        encrypt_str=po,
        nonce=data["nonce"],
        timestamp=data["timestamp"],
        signature=data["signature"]
    )

    callback = demjson.decode(callback)
    if callback["EventType"] == "user_add_org":
        # 添加员工
        app.logger.info('ding_talk EvenType: ', '添加员工事件！')
        print('sun_jia_jia: 有个狗B加入公司了')
    elif callback["EventType"] == "org_dept_create":
        # 添加部门
        app.logger.info('ding_talk EvenType: ', '添加部门事件！')
        print('sun_jia_jia: 有个狗B加入部门了')
    return jsonify(result)


if __name__ == '__main__':
    token = '123'  # 第三方企业应用中的Token
    aes_key = '123'  # 第三方企业应用中的加密密钥
    corp_id = '123'  # 企业id
    app_key = '123'
    app_secret = '123-mXOtZqnzlnFB44CAq'
    redis_ding = redis.StrictRedis('127.0.0.1', 6379)
    ding_client = AppKeyClient(corp_id, app_key, app_secret, storage=KvStorage(redis_ding))
    app.run(host='0.0.0.0', port=80, debug=True)
