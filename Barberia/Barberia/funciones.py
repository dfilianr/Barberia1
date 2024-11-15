class Opciones:
    def __init__(self):
        pass
    def planes(self):
        PLANES = (('B', 'Básico $3'), ('D', 'Deluxe $4'), ('V', 'VIP $8'))
        return PLANES

    def estado_civil(self):
        ESTADO_CIVIL = (('S','Soltero(a)'),('C','Casado(a)'),('D','Divorciado(a)'),
            ('V', 'Viudo(a)'),('U','Union Libre'),
        )
        return ESTADO_CIVIL
    def horario_atencion(self):
        horarioAtencion = (('1','10:00 a 11:00'),('2','11:00 a 12:00'),('3','13:00 a 14:00'),
                           ('4','14:00 a 15:00'),('5','15:00 a 16:00'),('6','16:00 a 17:00'),
                           ('7','17:00 a 18:00'),('8','18:00 a 19:00'),('9','19:00 a 20:00'),)
        return horarioAtencion