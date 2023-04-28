import module.custom_module as custom_module

rad = float(input("radius: "))
print("diameter {}".format(custom_module.diameter(rad)))
print("circumference {}".format(custom_module.circumference(rad)))
print("area {}".format(custom_module.area(rad)))