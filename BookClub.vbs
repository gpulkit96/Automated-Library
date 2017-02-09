Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Bookclub_V2.bat" & Chr(34), 0
Set WinScriptHost = Nothing