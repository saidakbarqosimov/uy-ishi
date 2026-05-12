set1 = {'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2 = {'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3 = {'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

natija = (set1 & set2) - set3
print(", ".join(natija)) 
