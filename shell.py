from news.models import *

User.objects.create_user('Pushkin')

User.objects.create_user('Gogol')

Author.objects.create(user_id=1)

Author.objects.create(user_id=2)

Category.objects.create(name='Поэзия')

Category.objects.create(name='Проза')

Category.objects.create(name='Сказка')

Category.objects.create(name='Анонс')

text1 = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
'''

pushkin = Author.objects.get(pk=1)

Post.objects.create(author=pushkin, message='A', title='У Лукоморья', text=text1)

text2 = '''Знаете ли вы украинскую ночь?
 О, вы не знаете украинской ночи!
  Всмотритесь в нее. 
  С середины неба глядит месяц. 
  Необъятный небесный свод раздался, раздвинулся еще необъятнее. 
  Горит и дышит он. 
  Земля вся в серебряном свете; и чудный воздух и прохладно-душен, и полон неги, и движет океан благоуханий. 
  Божественная ночь! Очаровательная ночь! 
  Недвижно, вдохновенно стали леса, полные мрака, и кинули огромную тень от себя. 
  Тихи и покойны эти пруды; холод и мрак вод их угрюмо заключен в темно-зеленые стены садов. 
  Девственные чащи черемух и черешен пугливо протянули свои корни в ключевой холод и изредка лепечут листьями, 
  будто сердясь и негодуя, когда прекрасный ветреник — ночной ветер, подкравшись мгновенно, целует их. 
  Весь ландшафт спит. А вверху все дышит, все дивно, все торжественно. 
  А на душе и необъятно, и чудно, и толпы серебряных видений стройно возникают в ее глубине. 
  Божественная ночь! Очаровательная ночь! 
  И вдруг все ожило: и леса, и пруды, и степи. 
  Сыплется величественный гром украинского соловья, и чудится, что и месяц заслушался его посереди неба... 
  Как очарованное, дремлет на возвышении село. 
  Еще белее, еще лучше блестят при месяце толпы хат; еще ослепительнее вырезываются из мрака низкие их стены. 
  Песни умолкли. Все тихо. Благочестивые люди уже спят. 
  Где-где только светятся узенькие окна. 
  Перед порогами иных только хат запоздалая семья совершает свой поздний ужин.'''

gogol = Author.objects.get(pk=2)

Post.objects.create(author=gogol, message='A', title='Тиха украинская ночь', text=text2)

text3 = 'Что за прелесть эти сказки. Каждая есть поэма!'

Post.objects.create(author=pushkin, message='N', title='Что за прелесть эти сказки', text=text3)

cat1 = Category.objects.get(pk=1)

cat2 = Category.objects.get(pk=2)

cat3 = Category.objects.get(pk=3)

cat4 = Category.objects.get(pk=4)

Post.objects.get(pk=1).category.add(cat1)

Post.objects.get(pk=1).category.add(cat3)

Post.objects.get(pk=2).category.add(cat2)

Post.objects.get(pk=3).category.add(cat4)

comm1 = 'Чудесно'
comm2 = 'Гениально'
comm3 = 'Ждем...'
comm4 = 'И где?'

Comment.objects.create(post=Post.objects.get(pk=1), author=gogol, text=comm2)

Comment.objects.create(post=Post.objects.get(pk=2), author=pushkin, text=comm1)

Comment.objects.create(post=Post.objects.get(pk=3), author=gogol, text=comm3)

Comment.objects.create(post=Post.objects.get(pk=3), author=gogol, text=comm4)

Post.objects.get(pk=1).like()

Post.objects.get(pk=1).like()

Post.objects.get(pk=2).like()

Post.objects.get(pk=3).like()

Post.objects.get(pk=3).dislike()

Comment.objects.get(pk=1).like()

Comment.objects.get(pk=1).like()

Comment.objects.get(pk=2).like()

Comment.objects.get(pk=3).like()

Comment.objects.get(pk=3).dislike()

Comment.objects.get(pk=4).dislike()

pushkin.update_rating()

gogol.update_rating()

rating_author = Author.objects.all().order_by('-rating').first()

print(f'Наибольший рейтинг у автора {User.objects.get(pk=rating_author.user_id).username}:  {rating_author.rating}')

rating_post = Post.objects.all().order_by('-rating').first()
print(f'''Лучшая статья:
\tДата добавления: {rating_post.time_in:%d.%m.%Y %H:%M:%S}
\tРейтинг: {rating_post.rating}
\tАвтор: {User.objects.get(pk=rating_post.author.user_id).username}
{rating_post.preview()}''')

rating_post_comments = Comment.objects.filter(post=rating_post)
print('Комментарии к лучшей статье:\n',
      '\n'.join([f'''\tДата добавления: {post.time_in:%d.%m.%Y %H:%M:%S}
      \tАвтор: {User.objects.get(pk=post.author.user_id).username}
      \tРейтинг: {post.rating}
      \tТекст: {post.text}''' for post in rating_post_comments]))



