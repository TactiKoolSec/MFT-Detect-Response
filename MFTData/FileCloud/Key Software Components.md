| **Key Software Components**                                             | **NOTES**                                                                                                                                                     |                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Web Hosting Process:**                                                | httpd.exe                                                                                                                                                     |                                                                                                                                                                                                                                                                                                          |
| **Web Hosting Process Parent:**                                         | services.exe                                                                                                                                                  |                                                                                                                                                                                                                                                                                                          |
| **Web Hosting Process grandparent:**                                    | winnit.exe                                                                                                                                                    |                                                                                                                                                                                                                                                                                                          |
| **Web Hosting Process Working Directory:**                              | C:\\xampp\\apache\\bin\\httpd.exe                                                                                                                             |                                                                                                                                                                                                                                                                                                          |
| **Web Hosting Process Command Line:**                                   | "C:\\xampp\\apache\\bin\\httpd.exe" -k runservice                                                                                                             |                                                                                                                                                                                                                                                                                                          |
| **Web Hosting Process grandparent:**                                    |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
| **Admin Portal:**                                                       | [http://127.0.0.1/ui/admin2/index.html\#/](http://127.0.0.1/ui/admin2/index.html#/)                                                                           | Admin URLs  http://\<your filecloud address or IP\>/admin (or) https://\<your filecloud address or IP\>/admin                                                                                                                                                                                            |
| **MFT Portal:**                                                         | [https://portal.getfilecloud.com/ui/user/index.html\#/loginhttp://127.0.0.1/ui/core/index.html\#/](https://portal.getfilecloud.com/ui/user/index.html#/login) |                                                                                                                                                                                                                                                                                                          |
| **Database Process:**                                                   | mongod.exe                                                                                                                                                    |                                                                                                                                                                                                                                                                                                          |
| **Database Child Process:**                                             | conhost.exe                                                                                                                                                   |                                                                                                                                                                                                                                                                                                          |
|                                                                         |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
| **Log Sources for Common Attacker Actions**                             | **NOTES**                                                                                                                                                     |                                                                                                                                                                                                                                                                                                          |
| **New User Creation:**                                                  | found in audit logs in browser                                                                                                                                |                                                                                                                                                                                                                                                                                                          |
| **Database Logs:**                                                      | C:\\xampp\\mongodb\\bin\\log                                                                                                                                  |                                                                                                                                                                                                                                                                                                          |
| **User Authentication Event to Admin Console:**                         | C:\\xampp\\apache\\logs\\access_\<year\>-\<month\>-\<date\>                                                                                                   |                                                                                                                                                                                                                                                                                                          |
| **Admin Console Access Logs:**                                          | C:\\xampp\\apache\\logs\\access_\<year\>-\<month\>-\<date\>                                                                                                   | ex: C:\\xampp\\apache\\logs\\access_23-07-31                                                                                                                                                                                                                                                             |
| **File Activity Events:**                                               | found in audit logs in browser                                                                                                                                |                                                                                                                                                                                                                                                                                                          |
|                                                                         |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
| **Command Execution via MFT Automation:**                               |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
| **Command Execution via MFT Automation Activity within MFT Datastore:** |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
| **Command Execution via MFT Auomation Activity within Logs:**           |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
|                                                                         |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
| **ADDITIONAL DATA**                                                     | **NOTES**                                                                                                                                                     |                                                                                                                                                                                                                                                                                                          |
| ![](media/ef4e87e5f6a90787bb9fa4481e496eae.png)**Version**              | 23.1.0.22597                                                                                                                                                  |                                                                                                                                                                                                                                                                                                          |
| **Default admin credentials**                                           | username: "admin" / pw: "password"                                                                                                                            |  https://www.filecloud.com/supportdocs/fcdoc/latest/server/filecloud-administrator-guide/installing-filecloud-server  resetting admin pass: https://www.filecloud.com/supportdocs/fcdoc/latest/server/filecloud-administrator-guide/filecloud-site-setup/administrator-settings/resetting-admin-password |
| **Default Install Dir**                                                 |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |
| **Default Ports**                                                       | webserver ports: 80, 443 database port: 27017                                                                                                                 |                                                                                                                                                                                                                                                                                                          |
| **Basic Installation requirements**                                     | <http://127.0.0.1/install/>                                                                                                                                   | INTERESTING!                                                                                                                                                                                                                                                                                             |
| **Documentation:**                                                      | <https://www.filecloud.com/supportdocs/fcdoc/latest/server>                                                                                                   |                                                                                                                                                                                                                                                                                                          |
| ![](media/206dd71ceb3111c70c3a9e2ef51482f9.png)                         |                                                                                                                                                               |                                                                                                                                                                                                                                                                                                          |

![](media/7c4fa4d19c47a3db759b86fea7f8bad2.png)

![](media/6ae82e7e38c4e67f6617f2dad58adff6.png)

![](media/b65b625823df708ac2ca31ee6d9bb8fe.png)![](media/2eebb2dcdb33d8d89f4691ec2ffa86ea.png)