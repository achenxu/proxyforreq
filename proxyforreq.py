def proxyforreq(proxy):

    try:
        proxy.split(":")[2]
        ip = proxy.split(":")[0]
        port = proxy.split(":")[1]
        userpassproxy = '%s:%s' % (ip, port)
        proxyuser = proxy.split(":")[2].rstrip()
        proxypass = proxy.split(":")[3].rstrip()
        proxies = {'http': 'http://%s:%s@%s' % (proxyuser, proxypass, userpassproxy),
                   'https': 'http://%s:%s@%s' % (proxyuser, proxypass, userpassproxy)}

    except:
        proxies = {'http': 'http://%s' % proxy, 'https': 'http://%s' % proxy}

    return proxies
