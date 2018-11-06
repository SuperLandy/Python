ha_conf= '''global
    log         127.0.0.1 local2                        
    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon
    stats socket /var/lib/haproxy/stats
defaults
    mode                    tcp
    log                     global
#    option                  httplog
#    option                  dontlognull
#    option http-server-close
    option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000
frontend mstsc
        bind 192.168.91.200:20000
        timeout client 100m
        default_backend mstsc-back
backend mstsc-back
        balance roundrobin
        server app1 192.168.91.131:3389 check
        '''

keep_conf = '''
global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
#   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

vrrp_instance sun {
    state BACKUP/MASTER
    interface ens33
    track interface ens33
    virtual_router_id 51
    priority 100
    advert_int 1
    preempt
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.91.200
    }
}'''
a =[]
print(keep_conf)
for a in keep_conf:

    a.apped