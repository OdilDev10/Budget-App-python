class Category():
    def __init__(self, nombre):
        self.nombre = nombre
        self.ledger = []
    
    def deposit(self, amount, description = '', account = 0):
        estado = {'amount': amount, 'description': description, 'account': account}
        self.ledger.append(estado) 
        print('Deposito Agregado Satisfactoriamente') 
        print('Estado de cuenta', self.ledger[account]['amount'])        
               
        return True
        
    def withdraw(self, amount, description = '', account = 0):
       
        estado = {'amount': amount, 'description': description, 'account': account}
        estadoCuenta = str(self.ledger[account]['amount'])
        
        
        if(float(estadoCuenta) < estado['amount']):
            print('Fondos insuficientes')
            print('Estado de cuenta', self.ledger[account]['amount'])        
            
            return False
        self.ledger[estado['account']]['amount'] = self.ledger[estado['account']]['amount'] - estado['amount']
        self.ledger[estado['account']]['desctiption'] = estado['description']
        print('Retiro Satisfactorio')
        print('Estado de cuenta', self.ledger[account]['amount'])        
        
        return True
    
    def check_funds(self, amount, account):
        if(amount > self.ledger[account]['amount']):
            return True
        return False
        
    
    def transfer(self, amount, description, account):
        estado = {'amount': amount, 'description': description, 'account': account}
        resultadoRetiro = self.withdraw(amount, description, account)
        if(resultadoRetiro == True):
            self.deposit(estado['amount'], estado['description'], estado['account'])
            return True
        return False
    
    def get_balance(self, numeroCuenta):
        return print('Estado de cuenta', self.ledger[numeroCuenta]['amount'])        





categoria = Category('Ledger')
categoria.deposit(100, 'Para estudiar', 0)
categoria.withdraw(50, 'Para estudiar', 0)
categoria.get_balance(0)
categoria.transfer(10, 'Transferir a Cuenta2', 0)
# categoria.check_funds(100, 0)