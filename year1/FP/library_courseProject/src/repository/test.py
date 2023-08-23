class Index( ):
    def __getitem__( self, key ):
        if not self.has_key( key ):
            super(Index,self).__setitem__( key, [] )
        return super(Index,self).__getitem__( key )
    def has_key(self, key):
        if key in super(Index, self).keys():
            return True
        return False


n = Index()
print(n)
n["a"] = 2
print(n)
print(n["b"])
print(n)
