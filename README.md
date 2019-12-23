# C2D
optimal solution to read  and save a config file.

## Install
  ```
  pip install C2D
  ```
## Usage
1. Import C2D
  ```
  from C2D import C2D
  ```
2. Create object
  ```
  config=C2D.C2D()
  ```
3. Create config.ini
  ```
  from C2D import C2D

  key={'section': {'name': 'c2d',
                  'version': '1.0'
                  },
        'install': {'date': '23/12/2019'}
      }
# Create C2D Object      
config=C2D.C2D(keys=key)
#This will Save config.ini file
config.Save()
  ```

  if you want to give custom file NAME
  ```
  config=C2D.C2D(file='Test.ini',keys=key)
  ```

4. Read Config File
  ```
  from C2D import C2D
  config=C2D.C2D()
  keys_values=config.Read()
  print(keys_values)
  ```
  Output
    ```
    {'section': {'name': 'c2d', 'version': '1.0'}, 'install': {'date': '23/12/2019'}}
    ```

  To Read a Custom file
  ```
  config=C2D.C2D(file='Test.ini')
  ```

5. Read All Sections

  ```
  from C2D import C2D
  config=C2D.C2D()
  config.Read()
  print(config.Sections())
  ```
  Output
    ```
    ['section', 'install']
    ```

6. Read Values By Section Name
  ```
  from C2D import C2D
  config=C2D.C2D()
  config.Read()
  print(config.Values('install'))

  ```
  Output
    ```
    {'date': '23/12/2019'}
    ```
## Help
  ```
  >>> help(C2D)
Help on module C2D.C2D in C2D:

NAME
    C2D.C2D

CLASSES
    builtins.object
        C2D

    class C2D(builtins.object)
     |  C2D(file='config.ini', keys=None, sep='=')
     |  
     |  C2D is an class for creating and reading config.ini files.
     |  
     |  Create Object:
     |  -------------
     |      obj=C2D(file='config.ini',keys=None,sep='=')
     |  
     |      Parameter:
     |      ---------
     |          file: optional,any File name ,default file name is config.ini
     |          sep : optional,separator,defualt separator is =
     |          key : optional,an Dictionary object
     |  
     |          key={
     |                'section': {
     |                  'name': 'c2d',
     |                  'version': '1.0'
     |                },
     |                'install': {
     |                  'date': '23/12/2019'
     |                }
     |              }
     |  Methods:
     |  -------
     |      obj.Save()    : save config file
     |      obj.Read()    : read config file and return config dict object.
     |      obj.Sections(): list of section in config.ini
     |      obj.Values()  : all avialable paramters and Values
  ```
