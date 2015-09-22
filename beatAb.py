s = Sandbox()

s.safe_modules = ['os', 'io', 'sys']
orgbuiltins["__import__"]=p._safe_import(__import__, safe_modules)
orgbuiltins["__import__"]=s._safe_import(__import__, safe_modules)

print(dir())

s.execute('import os; print("we good")')
