import Pages.Cases
import Pages.CommonData
import Pages.Devices
import Pages.Login
import Pages.Header
import Pages.Users
import Pages.Workspace

#Общая оболочка для всех класов
class Common_Class(Pages.Header.Header_Class, Pages.Login.Login_Page_Class,Pages.Workspace.Workspace_Class):
    LOGIN_1 = "dbadmin"
