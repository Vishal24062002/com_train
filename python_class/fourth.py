def log(msg):
    def logi():
        print('log',msg)
    return logi
ab=log('hi')
ab()