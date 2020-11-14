__all__ = ['lastregchk']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['n_letters', 'n_reg', 'c2', 'mapping', 'numeric_reg', 'c3', 'c1', 'full_alphabet', 'hl_reg', 'stride_reg', 'lookup', 'numeric_mappings', 'ja_reg', 'stride_mappings', 'n_letter', 'i', 'limited_alphabet'])
    @Js
    def PyJsHoisted_lookup_(hexid, this, arguments, var=var):
        var = Scope({'hexid':hexid, 'this':this, 'arguments':arguments}, var)
        var.registers(['hexid'])
        var.put('hexid', (+(Js('0x')+var.get('hexid'))))
        if var.get('isNaN')(var.get('hexid')):
            return var.get(u"null")
        var.put('reg', var.get('n_reg')(var.get('hexid')))
        if var.get('reg'):
            return var.get('reg')
        var.put('reg', var.get('ja_reg')(var.get('hexid')))
        if var.get('reg'):
            return var.get('reg')
        var.put('reg', var.get('hl_reg')(var.get('hexid')))
        if var.get('reg'):
            return var.get('reg')
        var.put('reg', var.get('numeric_reg')(var.get('hexid')))
        if var.get('reg'):
            return var.get('reg')
        var.put('reg', var.get('stride_reg')(var.get('hexid')))
        if var.get('reg'):
            return var.get('reg')
        return var.get(u"null")
    PyJsHoisted_lookup_.func_name = 'lookup'
    var.put('lookup', PyJsHoisted_lookup_)
    @Js
    def PyJsHoisted_stride_reg_(hexid, this, arguments, var=var):
        var = Scope({'hexid':hexid, 'this':this, 'arguments':arguments}, var)
        var.registers(['mapping', 'i1', 'hexid', 'i3', 'offset', 'i', 'i2'])
        pass
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('stride_mappings').get('length')):
            try:
                var.put('mapping', var.get('stride_mappings').get(var.get('i')))
                if ((var.get('hexid')<var.get('mapping').get('start')) or (var.get('hexid')>var.get('mapping').get('end'))):
                    continue
                var.put('offset', ((var.get('hexid')-var.get('mapping').get('start'))+var.get('mapping').get('offset')))
                var.put('i1', var.get('Math').callprop('floor', (var.get('offset')/var.get('mapping').get('s1'))))
                var.put('offset', (var.get('offset')%var.get('mapping').get('s1')))
                var.put('i2', var.get('Math').callprop('floor', (var.get('offset')/var.get('mapping').get('s2'))))
                var.put('offset', (var.get('offset')%var.get('mapping').get('s2')))
                var.put('i3', var.get('offset'))
                if ((((((var.get('i1')<Js(0.0)) or (var.get('i1')>=var.get('mapping').get('alphabet').get('length'))) or (var.get('i2')<Js(0.0))) or (var.get('i2')>=var.get('mapping').get('alphabet').get('length'))) or (var.get('i3')<Js(0.0))) or (var.get('i3')>=var.get('mapping').get('alphabet').get('length'))):
                    continue
                return (((var.get('mapping').get('prefix')+var.get('mapping').get('alphabet').callprop('charAt', var.get('i1')))+var.get('mapping').get('alphabet').callprop('charAt', var.get('i2')))+var.get('mapping').get('alphabet').callprop('charAt', var.get('i3')))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        return var.get(u"null")
    PyJsHoisted_stride_reg_.func_name = 'stride_reg'
    var.put('stride_reg', PyJsHoisted_stride_reg_)
    @Js
    def PyJsHoisted_numeric_reg_(hexid, this, arguments, var=var):
        var = Scope({'hexid':hexid, 'this':this, 'arguments':arguments}, var)
        var.registers(['reg', 'mapping', 'i', 'hexid'])
        pass
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('numeric_mappings').get('length')):
            try:
                var.put('mapping', var.get('numeric_mappings').get(var.get('i')))
                if ((var.get('hexid')<var.get('mapping').get('start')) or (var.get('hexid')>var.get('mapping').get('end'))):
                    continue
                var.put('reg', (((var.get('hexid')-var.get('mapping').get('start'))+var.get('mapping').get('first'))+Js('')))
                return (var.get('mapping').get('template').callprop('substring', Js(0.0), (var.get('mapping').get('template').get('length')-var.get('reg').get('length')))+var.get('reg'))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
    PyJsHoisted_numeric_reg_.func_name = 'numeric_reg'
    var.put('numeric_reg', PyJsHoisted_numeric_reg_)
    @Js
    def PyJsHoisted_n_letters_(rem, this, arguments, var=var):
        var = Scope({'rem':rem, 'this':this, 'arguments':arguments}, var)
        var.registers(['rem'])
        if (var.get('rem')==Js(0.0)):
            return Js('')
        var.put('rem',Js(var.get('rem').to_number())-Js(1))
        return (var.get('limited_alphabet').callprop('charAt', var.get('Math').callprop('floor', (var.get('rem')/Js(25.0))))+var.get('n_letter')((var.get('rem')%Js(25.0))))
    PyJsHoisted_n_letters_.func_name = 'n_letters'
    var.put('n_letters', PyJsHoisted_n_letters_)
    @Js
    def PyJsHoisted_n_letter_(rem, this, arguments, var=var):
        var = Scope({'rem':rem, 'this':this, 'arguments':arguments}, var)
        var.registers(['rem'])
        if (var.get('rem')==Js(0.0)):
            return Js('')
        var.put('rem',Js(var.get('rem').to_number())-Js(1))
        return var.get('limited_alphabet').callprop('charAt', var.get('rem'))
    PyJsHoisted_n_letter_.func_name = 'n_letter'
    var.put('n_letter', PyJsHoisted_n_letter_)
    @Js
    def PyJsHoisted_n_reg_(hexid, this, arguments, var=var):
        var = Scope({'hexid':hexid, 'this':this, 'arguments':arguments}, var)
        var.registers(['reg', 'digit2', 'hexid', 'digit3', 'digit4', 'offset', 'digit1'])
        var.put('offset', (var.get('hexid')-Js(10485761)))
        if ((var.get('offset')<Js(0.0)) or (var.get('offset')>=Js(915399.0))):
            return var.get(u"null")
        var.put('digit1', (var.get('Math').callprop('floor', (var.get('offset')/Js(101711.0)))+Js(1.0)))
        var.put('reg', (Js('N')+var.get('digit1')))
        var.put('offset', (var.get('offset')%Js(101711.0)))
        if (var.get('offset')<=Js(600.0)):
            return (var.get('reg')+var.get('n_letters')(var.get('offset')))
        var.put('offset', Js(601.0), '-')
        var.put('digit2', var.get('Math').callprop('floor', (var.get('offset')/Js(10111.0))))
        var.put('reg', var.get('digit2'), '+')
        var.put('offset', (var.get('offset')%Js(10111.0)))
        if (var.get('offset')<=Js(600.0)):
            return (var.get('reg')+var.get('n_letters')(var.get('offset')))
        var.put('offset', Js(601.0), '-')
        var.put('digit3', var.get('Math').callprop('floor', (var.get('offset')/Js(951.0))))
        var.put('reg', var.get('digit3'), '+')
        var.put('offset', (var.get('offset')%Js(951.0)))
        if (var.get('offset')<=Js(600.0)):
            return (var.get('reg')+var.get('n_letters')(var.get('offset')))
        var.put('offset', Js(601.0), '-')
        var.put('digit4', var.get('Math').callprop('floor', (var.get('offset')/Js(35.0))))
        var.put('reg', var.get('digit4').callprop('toFixed', Js(0.0)), '+')
        var.put('offset', (var.get('offset')%Js(35.0)))
        if (var.get('offset')<=Js(24.0)):
            return (var.get('reg')+var.get('n_letter')(var.get('offset')))
        var.put('offset', Js(25.0), '-')
        return (var.get('reg')+var.get('offset').callprop('toFixed', Js(0.0)))
    PyJsHoisted_n_reg_.func_name = 'n_reg'
    var.put('n_reg', PyJsHoisted_n_reg_)
    @Js
    def PyJsHoisted_hl_reg_(hexid, this, arguments, var=var):
        var = Scope({'hexid':hexid, 'this':this, 'arguments':arguments}, var)
        var.registers(['hexid'])
        if ((var.get('hexid')>=Js(7453184)) and (var.get('hexid')<=Js(7454617))):
            return (Js('HL')+((var.get('hexid')-Js(7453184))+Js(29184)).callprop('toString', Js(16.0)))
        if ((var.get('hexid')>=Js(7454720)) and (var.get('hexid')<=Js(7454873))):
            return (Js('HL')+((var.get('hexid')-Js(7454720))+Js(32768)).callprop('toString', Js(16.0)))
        if ((var.get('hexid')>=Js(7455232)) and (var.get('hexid')<=Js(7455385))):
            return (Js('HL')+((var.get('hexid')-Js(7455232))+Js(33280)).callprop('toString', Js(16.0)))
        return var.get(u"null")
    PyJsHoisted_hl_reg_.func_name = 'hl_reg'
    var.put('hl_reg', PyJsHoisted_hl_reg_)
    @Js
    def PyJsHoisted_ja_reg_(hexid, this, arguments, var=var):
        var = Scope({'hexid':hexid, 'this':this, 'arguments':arguments}, var)
        var.registers(['reg', 'digit2', 'hexid', 'digit3', 'letter3', 'offset', 'digit1'])
        var.put('offset', (var.get('hexid')-Js(8650752)))
        if ((var.get('offset')<Js(0.0)) or (var.get('offset')>=Js(229840.0))):
            return var.get(u"null")
        var.put('reg', Js('JA'))
        var.put('digit1', var.get('Math').callprop('floor', (var.get('offset')/Js(22984.0))))
        if ((var.get('digit1')<Js(0.0)) or (var.get('digit1')>Js(9.0))):
            return var.get(u"null")
        var.put('reg', var.get('digit1'), '+')
        var.put('offset', (var.get('offset')%Js(22984.0)))
        var.put('digit2', var.get('Math').callprop('floor', (var.get('offset')/Js(916.0))))
        if ((var.get('digit2')<Js(0.0)) or (var.get('digit2')>Js(9.0))):
            return var.get(u"null")
        var.put('reg', var.get('digit2'), '+')
        var.put('offset', (var.get('offset')%Js(916.0)))
        if (var.get('offset')<Js(340.0)):
            var.put('digit3', var.get('Math').callprop('floor', (var.get('offset')/Js(34.0))))
            var.put('reg', var.get('digit3'), '+')
            var.put('offset', (var.get('offset')%Js(34.0)))
            if (var.get('offset')<Js(10.0)):
                return (var.get('reg')+var.get('offset'))
            var.put('offset', Js(10.0), '-')
            return (var.get('reg')+var.get('limited_alphabet').callprop('charAt', var.get('offset')))
        var.put('offset', Js(340.0), '-')
        var.put('letter3', var.get('Math').callprop('floor', (var.get('offset')/Js(24.0))))
        return ((var.get('reg')+var.get('limited_alphabet').callprop('charAt', var.get('letter3')))+var.get('limited_alphabet').callprop('charAt', (var.get('offset')%Js(24.0))))
    PyJsHoisted_ja_reg_.func_name = 'ja_reg'
    var.put('ja_reg', PyJsHoisted_ja_reg_)
    var.put('limited_alphabet', Js('ABCDEFGHJKLMNPQRSTUVWXYZ'))
    var.put('full_alphabet', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    var.put('stride_mappings', Js([Js({'start':Js(32785),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('ZS-')}), Js({'start':Js(3735552),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('F-G')}), Js({'start':Js(3768320),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('F-H')}), Js({'start':Js(3949601),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('D-A'),'first':Js('AAA'),'last':Js('OZZ')}), Js({'start':Js(3932161),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-A'),'first':Js('PAA'),'last':Js('ZZZ')}), Js({'start':Js(3965985),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('D-B'),'first':Js('AAA'),'last':Js('OZZ')}), Js({'start':Js(3940353),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-B'),'first':Js('PAA'),'last':Js('ZZZ')}), Js({'start':Js(3981312),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-C')}), Js({'start':Js(3998888),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-E')}), Js({'start':Js(4016464),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-F')}), Js({'start':Js(4034040),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-G')}), Js({'start':Js(4051616),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-H')}), Js({'start':Js(4069192),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('D-I')}), Js({'start':Js(4490273),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('OO-')}), Js({'start':Js(4555809),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('OY-')}), Js({'start':Js(4587520),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('OH-')}), Js({'start':Js(4621345),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('SX-')}), Js({'start':Js(4785185),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('CS-')}), Js({'start':Js(4850721),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('YR-')}), Js({'start':Js(4949025),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('TC-')}), Js({'start':Js(7603233),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('JY-')}), Js({'start':Js(7734305),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('AP-')}), Js({'start':Js(7767073),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('9V-')}), Js({'start':Js(7832609),'s1':Js(1024.0),'s2':Js(32.0),'prefix':Js('YK-')}), Js({'start':Js(12582913),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('C-F')}), Js({'start':Js(12600489),'s1':(Js(26.0)*Js(26.0)),'s2':Js(26.0),'prefix':Js('C-G')}), Js({'start':Js(14684225),'s1':Js(4096.0),'s2':Js(64.0),'prefix':Js('LV-')})]))
    var.put('numeric_mappings', Js([Js({'start':Js(1310720),'first':Js(0.0),'count':Js(100000.0),'template':Js('RA-00000')}), Js({'start':Js(721896),'first':Js(1000.0),'count':Js(1000.0),'template':Js('CU-T0000')})]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('stride_mappings').get('length')):
        try:
            var.put('mapping', var.get('stride_mappings').get(var.get('i')))
            if var.get('mapping').get('alphabet').neg():
                var.get('mapping').put('alphabet', var.get('full_alphabet'))
            if var.get('mapping').get('first'):
                var.put('c1', var.get('mapping').get('alphabet').callprop('indexOf', var.get('mapping').get('first').callprop('charAt', Js(0.0))))
                var.put('c2', var.get('mapping').get('alphabet').callprop('indexOf', var.get('mapping').get('first').callprop('charAt', Js(1.0))))
                var.put('c3', var.get('mapping').get('alphabet').callprop('indexOf', var.get('mapping').get('first').callprop('charAt', Js(2.0))))
                var.get('mapping').put('offset', (((var.get('c1')*var.get('mapping').get('s1'))+(var.get('c2')*var.get('mapping').get('s2')))+var.get('c3')))
            else:
                var.get('mapping').put('offset', Js(0.0))
            if var.get('mapping').get('last'):
                var.put('c1', var.get('mapping').get('alphabet').callprop('indexOf', var.get('mapping').get('last').callprop('charAt', Js(0.0))))
                var.put('c2', var.get('mapping').get('alphabet').callprop('indexOf', var.get('mapping').get('last').callprop('charAt', Js(1.0))))
                var.put('c3', var.get('mapping').get('alphabet').callprop('indexOf', var.get('mapping').get('last').callprop('charAt', Js(2.0))))
                var.get('mapping').put('end', ((((var.get('mapping').get('start')-var.get('mapping').get('offset'))+(var.get('c1')*var.get('mapping').get('s1')))+(var.get('c2')*var.get('mapping').get('s2')))+var.get('c3')))
            else:
                var.get('mapping').put('end', ((((var.get('mapping').get('start')-var.get('mapping').get('offset'))+((var.get('mapping').get('alphabet').get('length')-Js(1.0))*var.get('mapping').get('s1')))+((var.get('mapping').get('alphabet').get('length')-Js(1.0))*var.get('mapping').get('s2')))+(var.get('mapping').get('alphabet').get('length')-Js(1.0))))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('numeric_mappings').get('length')):
        try:
            var.get('numeric_mappings').get(var.get('i')).put('end', ((var.get('numeric_mappings').get(var.get('i')).get('start')+var.get('numeric_mappings').get(var.get('i')).get('count'))-Js(1.0)))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    return var.get('lookup')
PyJs_anonymous_0_._set_name('anonymous')
var.put('registration_from_hexid', PyJs_anonymous_0_())
if PyJsStrictNeq(var.get('module',throw=False).typeof(),Js('undefined')):
    var.get('module').put('exports', var.get('registration_from_hexid'))
pass


# Add lib to the module scope
lastregchk = var.to_python()