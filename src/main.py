from similarity import model 
m = model.similarity()
a = m.compute("The cat sits outside","A  man is playing guitar")
print(float(a.item())) 