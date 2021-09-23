from django.contrib import admin
from .models import Cart, Order, Product, ProductInCart, Deal
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProductInCartInLine(admin.TabularInline):
    model = ProductInCart

class CartInLine(admin.TabularInline):
    model = Cart

class DealInLine(admin.TabularInline):
  model = Deal.user.through

# class UserAdmin(UserAdmin):
#   model = User
#   list_display = ('username','get_cart', 'is_staff', 'is_active')
#   list_filter = ('username', 'is_staff', 'is_active')

#   fieldsets = (
#       (None, { 'fields': ('username', 'password',)}),
#       ('Permissions', {'fields': ('is_staff', ('is_active', 'is_superuser'),)}),
#       ('Important Dates', {'fields':('date_joined', 'last_login',)}),
#       ('Advanced Options', {
#         'classes': ['collapse in'],
#         'fields' : ['user_permissions', 'groups'],
#       }),
#       )

#   add_fieldsets = (
#       (None, {
#         'classes':'wide', 
#         'fields': ('username', 'password','is_staff')
#         }),
#   )

#   inlines = [
#       CartInLine, DealInLine,
#   ]

#   def get_cart(self, obj):
#     return obj.cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
  model = Cart
  list_display = ('user','staff', 'created_on')
  list_filter = ('user__is_staff','user', 'created_on')

  fieldsets = (
      ("Add to Cart", { 'fields': ('user', 'created_on',)}),
      )

  inlines = (
      ProductInCartInLine,
  )

  def staff(self, obj):
      return obj.user.is_staff

  staff.admin_order_field = 'user__is_staff'
  staff.short_description = "Staff (Coumn Heading)"

  search_fields = ('user__username','user__is_staff','created_on')


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
  inlines = (
      DealInLine,
  )
#   exclude = ('user',)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(Product)
# admin.site.register(Cart)
admin.site.register(ProductInCart)
admin.site.register(Order)
# admin.site.register(Deal)
