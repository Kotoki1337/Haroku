import win32com.client
import pythoncom

def checkExsit(process_name):
    pythoncom.CoInitialize()
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        processOnline = True
    else:
        processOnline = False

    return processOnline