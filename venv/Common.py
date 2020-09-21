import Pages.Cases
import Pages.CommonData
import Pages.Devices
import Pages.Login
import Pages.Space
import Pages.Users
import Pages.Workspace

#Общая оболочка для всех класов
class Common_Class(Pages.Space.Space_Class, Pages.Login.Login_Page_Class):
    LOGIN_1 = "dbadmin"
