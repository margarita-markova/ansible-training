from ansible.module_utils.basic import AnsibleModule
import psutil
import requests
import re


def proc_info(process, usr):
    statuses = []
    pids = [proc.pid for proc in psutil.process_iter() if proc.username() == usr and proc.name() == process]
    if pids:
        for pid in pids:
            statuses.append(psutil.Process(pid).status())
    return statuses


def port_handled(process, port):
    connections = []
    for conn in psutil.net_connections():
        if conn.laddr.port != port:
            continue
        proc_name = psutil.Process(conn.pid).name()
        if proc_name == process and conn.status == pstuil.CONN_LISTEN:
            connections.append(conn)
    return connections


def web_content(url, regexp):
    text = requests.get(url).text
    regexp = re.compile(regexp)
    return regexp.findall(text)


def web_info(request, regexp):
    regexp = re.compile(regexp)
    headers = {}
    for name, value in requests.get(url).headers:
        if regexp.findall(value):
            headers[name] = value
    return headers


def main():
    argument_spec = {
        'procname': {'type': 'str', 'required': True},
        'usrname': {'type': 'str', 'required': True},
        'port': {'type': 'str', 'required': False},
        'url': {'type': 'str', 'required': False, 'default': ""},
        'regexp': {'type': 'str', required: False, 'default': ""},
        'enable_server_info': {'type': 'boolean', 'default': "False"}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_together=[
            ['procname', 'usrname', 'port'],
            ['url', 'enable_server_info'],
        ],
        supports_check_mode=False
    )

    procname = module.params['procname']
    usrname = module.params['usrname']
    port = module.params['port']
    url = module.params['url']
    enable_server_info = module.params['enable_server_info']
    regexp = module.params['regexp']

    result = dict()

    result["changed"] = False
    result["process name"] = procname
    result["username"] = usrname

    if not proc_info(procname, usrname):
        result["status"] = "not exists"
        module.exit_json(**result)
    else:
        result["status"] = statuses[0]
        if ports:
            process_handled(procname,port)
        
        if not url:
            if not regexp:
                module.exit_json(**result)
            else:
                result["regex"] = regexp
                module.exit_json(**result)
        else:
            result["web content"] = web_content(url, regexp)

        if enable_server_info:
            result["server info"] = web_info(url, regexp)

    module.exit_json(**result)

if __name__ == '__main__':
    main()
