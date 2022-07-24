import pandas as pd
import numpy as np
import streamlit as st


st.markdown("<h1 style='text-align: center; color: black;'>Лабораторная работа</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Анализ рыночной корзины и ассоциативные правила </h2>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>или почему пиво покупают вместе с подгузниками</h6>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("screensaver.png")

with col3:
    st.write("")

st.markdown("<h5 style='text-align: center; color: black;'>Что такое поиск ассоциативных правил</h5>", unsafe_allow_html=True)
st.write("""Ассоциативное правило - правило для количественного описания взаимной связи между двумя или более событиями.

В 1992 году группа по консалтингу в области ритейла провела исследование 1.2 миллиона транзакций в 25магазинах у дома. После анализа всех этих транзакций самым сильным правилом получилось "Между 17:00 и 19:00 чаще всего пиво и подгуздники покупают вместе"

Анализ рыночной корзины — процесс поиска наиболее типичных ассоциативных правил покупок в супермаркетах. Он производится путем анализа баз данных транзакций с целью определения комбинаций товаров, связанных между собой. Иными словами, выполняется обнаружение товаров, наличие которых в транзакции влияет на вероятность появления других товаров или их комбинаций.

Результаты, полученные с помощью анализа рыночной корзины, позволяют оптимизировать ассортимент товаров и запасы, размещение их в торговых залах, увеличивать объемы продаж за счет предложения клиентам сопутствующих товаров. Например, если в результате анализа будет установлено, что совместная покупка макарон и кетчупа является типичным шаблоном, то разместив эти товары на одной и той же витрине можно «спровоцировать» покупателя на их совместное приобретение.""")

st.markdown("<h5 style='text-align: center; color: black;'>Список ассоциативных правил</h5>", unsafe_allow_html=True)

st.write("""Support (поддержка) 

В общем виде это показатель "частотности" данного товара во всех анализируемых транзакциях""")

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("support.png")

with col3:
    st.write("")
    
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("example_table.png")

with col3:
    st.write("")

st.write("""supp(e) = 8/10 = 0.8 """)
st.write("""supp(b & d) = 2/10 = 0.2 """)
st.write("""supp(b & d & e) = 2/10 = 0.2 """)

st.write("""Confidence (достоверность) 

Показатель того, как часто наше правило срабатывает для всего датасета""")
    
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("confidence.png")

with col3:
    st.write("")

st.write("""conf(b & d => e) = supp(b & d & e)/ supp(b & d) = 0.2/0.2 = 1 """)
st.write("""conf(e => b & d) = supp(b & d & e)/ supp(e) = 0.2/0.8 = 0.25 """)

st.write("""Lift (полезность правила) 

Показатель насколько товары зависят друг от друга""")
    
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("lift.png")

with col3:
    st.write("")

st.write("""lift(b => d) = supp(b & d)/ (supp(b) * supp(d)) = 0.2/(0.6 * 0.5) = 0.67 """)


st.markdown("<h5 style='text-align: left; color: black;'>Задание 1: </h5>", unsafe_allow_html=True)
st.write("""Посчитайте Lift(a => e)""")

answer = st.text_input("""Полезность правила(a => e):""")
if answer == "0.69":
    st.write("Задание решено")
else:
    st.write("Задание пока не решено")
    
st.markdown("<h5 style='text-align: center; color: black;'>Поиск ассоциативных правил. Алгоритм Apriori</h5>", unsafe_allow_html=True)

st.write("""Алгоритм Apriori -  алгоритмом, который применяется для получения ассоциативных правил.

На первом шаге алгоритма подсчитываются 1-элементные часто встречающиеся наборы. Для этого необходимо пройтись по всему набору данных и подсчитать для них поддержку, т.е. сколько раз встречается в базе.

Apriori использует следующее утверждение:""")

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("apriori-rule1.png")

with col3:
    st.write("")
st.write("""Из него следует:

Если Y встречается часто, то любое подмножество X так же встречается часто, если X встречается редко, то любое супермножество Y так же встречается редко.""")

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")

with col2:
    st.image("example_table.png")

with col3:
    st.write("")
    
st.write("""supp(a) = 0.7 """)
st.write("""supp(b) = 0.7 """)
st.write("""supp(c) = 0.5 """)
st.write("""supp(d) = 0.6 """)
st.write("""supp(e) = 0.8 """)
st.write("""Если нам нужны товары с частотой встречаемостью больше 0.6, мы можем отбросить все комбинации содержащие товары c и d. """)

st.markdown("<h6 style='text-align: center; color: black;'>Алгоритм Apriori</h6>", unsafe_allow_html=True)
st.write("""F1 = {Часто встречающиеся 1-элементные наборы}; """)

st.markdown("<h5 style='text-align: left; color: black;'>Задание 2: </h5>", unsafe_allow_html=True)
st.write("""Найдите комбинацию товаров, с наибольшей совместной частотой покупки (support) и наибольшей достоверностью (confidence). В качестве ответа укажите значение support и confidence этих товаров. """)

groceries  = pd.read_csv("groceries.txt", sep="\t")
groceries.drop(['Unnamed: 0'], axis=1, inplace=True)
groceries

support = st.text_input("""Support""")
confidence = st.text_input("""confidence""")
if support == "0.2" and confidence == "0.81":
    st.write("Задание решено")
else:
    st.write("Задание пока не решено")
  

st.markdown("<h5 style='text-align: center; color: black;'>Другие области применения</h5>", unsafe_allow_html=True)   
st.write("""Market basket analysis может применяться не только при анализе покупательской карзины, но и во многих других местах, где необходимо найти закономерности между событиями.""")
st.write("""Рассмотрим пример применения  market basket analysis для поиска фильмов наиболее часто смотрящих вместе""")

columns = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=columns)
columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv('u.item', sep='|', names=columns, encoding='latin-1')
movie_names = movies[['item_id', 'movie title']]
combined_movies_data = pd.merge(df, movie_names, on='item_id')
combined_movies_data = combined_movies_data[['user_id','movie title']]
st.dataframe(combined_movies_data.head(8))

st.write("""Посмотрим на комбинацию фильмов, которые чаще всего смотрят вместе""")
rules = pd.read_csv("rules.csv")
st.dataframe(rules.head())

st.write("""А теперь посмотрим фильмы, которые чаще всего смотрят после просмотра фильма "101 далматинец" """)
st.dataframe(rules[rules.antecedents.apply(str).str.contains("101 Dalmatians")].sort_values('lift', ascending=False))