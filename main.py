import streamlit as st
from PIL import Image
import pandas as pd

## ---------- 被験者情報の入力 ---------- ##
answer_dict = {}

ID = st.text_input('被験者番号を入力してください（半角数字）')
answer_dict["ID"] = ID
st.write("")
st.write("")

date_01 = "2022年6月13日"
date_02 = "2022年6月14日"
date = st.radio(
    "実験実施日を選択してください",
    (date_01, date_02))

if date == date_01:
    answer_dict["date"] = 20220613
else:
    answer_dict["date"] = 20220614

st.write("")
st.write("")

## ---------- 回答 ---------- ##
st.subheader("質問への回答")

def buttom():
    A = f'タイプ A　(NO.{i}-{j})'
    B = f'タイプ B　(NO.{i}-{j})'

    choice = st.radio(
     "好ましいユニットくじを選択してください",
     (A, B))

    if choice == A:
        answer_dict[f"{i}_{j}"] = 0
    else:
        answer_dict[f"{i}_{j}"] = 1

for i in range(1, 25):
    for j in range(1, 7):
        st.image( f"unitAB_{i}_{j}.png")
        buttom()
        st.write("")
        st.write("")


## ---------- 回答結果の出力 ---------- ##
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

output_dict={}
for k,v in answer_dict.items():   # 一度pd.Seriesに変換
    output_dict[k]=pd.Series(v)

df = pd.DataFrame(output_dict)

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name= f'UnitLottery_Answer_{ID}.csv',
     mime='text/csv',
 )