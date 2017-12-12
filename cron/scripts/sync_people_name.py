from pypinyin import lazy_pinyin

from people.models import People


for people in People.objects.all():
    people.update(pinyin=' '.join(lazy_pinyin(people.name)))


