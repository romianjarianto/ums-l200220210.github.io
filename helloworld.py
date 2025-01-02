from metaflow import FlowSpec, step

class KuliahFlow(FlowSpec):

    @step
    def start(self):
        """Bayar SPP"""
        print("Bayar SPP")
        self.next(self.a)

    @step
    def a(self):
        """Isi KRS"""
        print("Isi KRS")
        self.next(self.b)
      
    @step
    def b(self):
        """Konfirmasi PA"""
        print("Konfirmasi PA")
        self.next(self.c)
    
    @step
    def c(self):
        """KBM"""
        print("KBM")
        self.next(self.d)

    @step
    def d(self):
        """Mengikuti UTS dan UAS"""
        print("Mengikuti UTS dan UAS")
        self.next(self.end)
    @step
    def end(self):
        """Dapat KHS"""
        print("Dapat KHS")

if __name__ == '__main__':
    KuliahFlow()