class C2D:
    '''C2D is an class for creating and reading config.ini files.

    Create Object:
    -------------
        obj=C2D(file='config.ini',keys=None,sep='=')

        Parameter:
        ---------
            file: optional,any File name ,default file name is config.ini
            sep : optional,separator,defualt separator is = 
            key : optional,an Dictionary object

            key={
                  'section': {
                    'name': 'c2d',
                    'version': '1.0'
                  },
                  'install': {
                    'date': '23/12/2019'
                  }
                }
    Methods:
    -------
        obj.Save()    : save config file
        obj.Read()    : read config file and return config dict object.
        obj.Sections(): list of section in config.ini
        obj.Values()  : all avialable paramters and Values

    '''
    
    def __init__(self,file='config.ini',keys=None,sep='='):
        self.file=file
        self.config={}
        self.sep=sep
        self.keys=keys

                
    def Save(self):
        '''Save the Config file 
        '''
        try:
            with open(self.file,'wt') as file:
                line=0
                for section,parameter in self.keys.items():
                    if line !=0:
                        file.write("\n\n")
                    file.write(f'[{section}]')
                    for key,value in parameter.items():
                        file.write(f'\n{key}{self.sep}{value}')
                        line+=1
                file.write('\n')
                return True
        except Exception as ex:
            return ex

    def Read(self):
        '''Read config file from self.file
        Output:
        ------
            Return an Dictionary Object containg all sections with their Values
        '''
        try:
            with open(self.file,'rt') as file:
                for sections in file.read().split('\n\n'):
                    splited_text=sections.split() 
                    section=splited_text[0][1:-1]
                    parameter={}
                    for val in splited_text[1:]:
                        key,value=val.split(self.sep)
                        parameter[key]=value
                    self.config[section]=parameter
                return self.config
        except Exception as ex:
            return ex
        
    def Sections(self):
        '''Read Section list from self.file
        Output:
        ------
            Return an list Object containg all sections names
        '''
        try:
            return list(self.config.keys())
        except Exception as ex:
            return ex

    def Values(self,section):
        '''Return particular Section Value
        Input:
        ------
            section:section name
            
        Output:
        ------
            Return an Dictionary Object containg all sections values.
            Return Error if Section is not Present
        '''
        if section not in self.Sections():
            return f"Section is Not Avialable in {self.file}"
        else:
            try:
                return self.Read()[section]
            except Exception as ex:
                return ex
                
c=C2D()
c.Read()
print(c.Sections())
print(c.Values('section'))
        
