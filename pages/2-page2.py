import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


#검색창에 anilist의 단어 일부가 일치하면 list의 해당 이미지를 출력하라

search = st.text_input('단어를 입력하세요')
st.write(search)

# if search:
#     for i in range(len(ani_list)):
#         if search in ani_list[i]:
#             st.image(img_list[i])
#             break

if search != '':
    for i in range(len(ani_list)):
        if search in ani_list[i]:
            st.image(img_list[i])
