COLOR 8A

@echo.
@echo.

@echo      正在启动odoo服务...

SETLOCAL

@cls
@echo ==========================================================
@echo.
@echo.
@echo      应用服务器已经启动完毕，请勿关闭此窗口！！！
@echo.
@echo      请在浏览器地址栏输入： http://localhost:8069 访问odoo13
@echo.
@echo      默认数据库（cwbase3）的用户名和密码：
@echo.
@echo      用户名： kongrui1@163.com
@echo.
@echo      密  码： aaaaaa
@echo.
@echo.
@echo ==========================================================
@echo off

F:\odoo\odoo13\venv\Scripts\python odoo-bin -c  odoo.conf

ENDLOCAL

pause
