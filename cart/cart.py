from ecom.models import Product,Profile

class Cart():
    def __init__(self,request):
        self.session = request.session
        
        self.request = request
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart=cart
        
    def db_add(self,product,quantity):
        product_id=str(product)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]= int(product_qty)
        
        self.session.modified =True
        
        if self.request.user.is_authenticated:
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            current_user.update(old_cart=str(carty))
            
    def add(self,product,quantity):
        product_id=str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]= int(product_qty)
        
        self.session.modified =True
        
        if self.request.user.is_authenticated:
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            current_user.update(old_cart=str(carty))
        
    def __len__(self):
        return len(self.cart)
    
    def add_prod(self):
        product_id = self.cart.keys()
        
        
        products = Product.objects.filter(id__in=product_id) #Field lookups
        
        return products
    
    def add_qty(self):
        quantities = self.cart
        return quantities
    
    def update(self,product,quantity):
        product_id=str(product)
        product_qty = int(quantity)
        
        other = self.cart
        
        other[product_id] = product_qty
        
        self.session.modified = True
        
        things= self.cart
        
        if self.request.user.is_authenticated:
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            current_user.update(old_cart=str(carty))
        
        return things
    
    def delete(self,product):
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
        
        if self.request.user.is_authenticated:
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            current_user.update(old_cart=str(carty))