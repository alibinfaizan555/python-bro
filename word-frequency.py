par = '''Poetry is the language of the imagination and the passions. It relates to whatever gives immediate pleasure or pain to the human mind. It comes home to the bosoms and businesses of men; for nothing but what comes home to them in the most general and intelligible shape can be a subject for poetry. Poetry is the universal language which the heart holds with nature and itself. He who has a contempt for poetry cannot have much respect for himself, or for anything else. Wherever there is a sense of beauty, or power, or harmony, as in the motion of a wave of the sea, in the growth of a flower, there is poetry in its birth'''
lo_par = par.lower()
d = {}
for i in lo_par.split():
  d[i] = d.get(i, 0) + 1

for key in d:
  print('"{}" occurs {} time(s).'.format(key, d[key]))
