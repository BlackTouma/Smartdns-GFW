# 将gfw-list解析成SmartDNS可用的格式

content = open("./gfw.conf")
with open("./gfw.smartdns.conf", "w+") as c:
    c.truncate(0)
    for line in content:
        c.write("nameserver /" + line.rstrip('\n') + "/GFW\n")

content.close()
exit()
