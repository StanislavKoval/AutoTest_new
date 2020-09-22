import Common

bb=Common.Common_Class()
print("Старт Тест 2")
bb.system_Log_In()

bb.open_workspace()
bb.save_grid_counter()

bb.close_site()
print("Финиш Тест 2")