class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points(1,2)
p1.print_point()


#############333

class Points(object):

  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x='A'

p2.print_point()


############

class Rectangle(object):
    
    def __init__(self,width=2,height =3,color='r'):
        self.height=height 
        self.width=width
        self.color=color
    
    def drawRectangle(self):
        import matplotlib.pyplot as plt
        plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()