import torch
# i need tool to inspect one package.
# it is accessible, via .__all__
# really funny.
# consider text writing as multidimentional. espec+-ially in source code composition.
# use ipython3?
# that is wrong. i always make the same mistake.
# it would be problematic.
# it only appends those with modules, but does not append those without a module.
# i think i need to sample those modules.
t = torch.FloatTensor([23, 24, 24.5])
p = t.size()
print(p)
x = torch.rand(10)
y = x.size()
print(y)
# boston_tensor= torch.from_numpy(boston.data)
# print(boston_tensor)