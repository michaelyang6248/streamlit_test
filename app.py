import pymysql
import csv
import pandas as pd
from datetime import datetime as dt , timedelta
# from xlsx2html import xlsx2html
from openpyxl import Workbook
import os , sys
import webbrowser
import numpy as np
import random
import json

import streamlit as st

# @st.cache()

tab1, tab2 , tab3 = st.tabs(['Examples','SAR','Excel'])
with tab1 :
    st.header('Examples')
    # st.image('https://static.streamlit.io/examples/cat.jpg')
    
    # Text Input
    
    title = st.text_input('[Text Input] 내용을 입력하세요')
    if title :
        st.write(title)
        
    title_pw = st.text_input('[Password Input] 암호를 입력하세요',type="password")
    # if title_pw :
    #     st.write(title_pw)
    
    your_message = st.text_area("[메모장" , placeholder="간단한 내용을 작성해 주세요")
    if your_message:
        st.write(your_message)
    
    col1 , col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
        "Start Date",
        dt(2024,12,31))
    with col2:
        end_date = st.date_input(
        "End Date",
        dt(2025,12,31))
    if not start_date :
        st.write('시작일을 다시 입력해 주세요')
    else:
        st.write('Start Date : ',start_date)
    
    if not end_date :
        st.write('종료일을 다시 입력해 주세요')
    else:
        st.write('End Date : ',end_date)
        
    # 파일 업로드(이미지)
    uploaded_file = st.file_uploader('Upload your Image file here...', type=['png','jpeg','jpg'])
    if uploaded_file is not None :
        st.image(uploaded_file)
    
    
    
    
    
    check_agree = st.checkbox('[체크박스] 동의하십니까?')
    if check_agree :
        st.write("동의해 주셔서 감사합니다. :100:")
        # st.dataframe(df,
        #         column_config={
        #             "Report" : st.column_config.LinkColumn(
        #                 label = "Report",
        #                 width ="None",
        #                 help="If you click the link, go to the Report",
        #                 display_text="Click"
        #             )
        #         },
        #         hide_index=True,             
        #         )

    #라디오 선택 버튼
    mbti = st.sidebar.radio(
        '[라디오박스] 당신의 MBTI는 무엇입니까?' ,
        ('ISTJ' , 'ENFP' , '선택지 없음'),
        index=2) # Default값 index값 할당 0,1,2
    if mbti == 'ISTJ':
        st.sidebar.write('당신은 :blue[현실주의자] 이시네요')
    elif mbti == 'ENFP':
        st.sidebar.write('당신은 :green[활동가] 이시네요')
    else:
        st.sidebar.write('당신에 대해 :red[알고 싶어요]:grey_exclamation:')


    # 선택박스 버튼(DropBox)
    mbti = st.sidebar.selectbox(
        '[단일선택] 당신의 MBTI는 무엇입니까?' ,
        ('ISTJ' , 'ENFP' , '선택지 없음'),
        index=2) # Default값 index값 할당 0,1,2
    if mbti == 'ISTJ':
        st.sidebar.write('당신은 :blue[현실주의자] 이시네요')
    elif mbti == 'ENFP':
        st.sidebar.write('당신은 :green[활동가] 이시네요')
    else:
        st.sidebar.write('당신에 대해 :red[알고 싶어요]:grey_exclamation:')
        
    # 다중 선택 박스
    options = st.multiselect(
        '[다중 선택] 당신이 좋아하는 과일은 뭔가요?',
        ['망고','오렌지','사과','바나나'],    
        ['망고','오렌지'])

    st.write(f'당신의 선택은: :red[{options}] 입니다.')

    #슬라이더
    values = st.slider(
        '[슬라이더] 범위의 값을 다음과 같이 지정할 수 있어요:sparkles:',
        0.0,100.0, (25.0, 75.0))
    st.write('선택범위 : ', values)

    #슬라이더 응용 ( 약속 시간 )
    start_time = st.slider(
        '[슬라이더_응용]언제 약속을 잡는 것이 좋을까요?',
        min_value=dt(2024, 1, 1, 0, 0),
        max_value=dt(2024, 12, 31 , 23 , 0),
        value=dt(2024, 12, 10, 16, 0),
        step=timedelta(hours=1), # 하루씩 이동하기 step=timedelta(days=1),
        format="MM/DD/YY - HH:mm")    
    st.write("선택한 약속 시간 : ", start_time)

    #텍스트 입력
    title = st.text_input(
        label='[텍스트 입력] 가고 싶은 여행지가 있나요?',
        placeholder='여행지를 입력해 주세요'
        )
    st.write(f'당신이 선택한 여행지 : :violet[{title}]')

    # 숫자 입력
    number = st.number_input(
        label = '[숫자입력] 나이를 입력해 주세요.',
        min_value=10,
        max_value=150,
        value=30,
        step=1
    )
    st.write('당신이 입력하신 나이는 : ', number)

    # st.dataframe(df,
    #              column_config={
    #                  "Report" : st.column_config.LinkColumn(
    #                      label = "Report",
    #                      width ="None",
    #                      help="If you click the link, go to the Report",
    #                      display_text="Click"
    #                  )
    #              },
    #              hide_index=True,             
    #              )

    # 로또생성기
    st.title(':sparkles:로또 생성기:sparkles:')
    def generate_lotto():
        lotto = set()
        
        while len(lotto) < 6 :
            number = random.randint(1,46)
            lotto.add(number)
        lotto = list(lotto)
        lotto.sort()
        return lotto

    st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {dt.now().strftime('%Y-%m-%d %H:%M')}")

    button = st.button('로또를 생성해 주세요!')
    if button :
        for i in range(1,6) :
            st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
        st.write(f"생성된 시각: {dt.now().strftime('%Y-%m-%d %H:%M')}")

with tab2 :
    st.header('SAR')
    # st.image('https://static.streamlit.io/examples/dog.jpg')
    coverity_trs_server_addr = 'idedqe.lge.com' # host='10.19.218.22'

    # connect = pymysql.connect(host= vpdsfile_NAS_server, port=3307 user='idsdet', password='Lge123456!', db='trs',charset='utf8mb4')
    connect = pymysql.connect(host=coverity_trs_server_addr, user='idsdet', password='bmdAZGhPxX2U5Euv', db='trs',charset='utf8mb4')
    cur = connect.cursor()

    today_dt_str = dt.today().strftime('%Y_%m_%d %H:%M:%S')

    # query = 'SELECT * FROM trs'
    query_find_person = "SELECT * FROM static_analysis_email WHERE email='michael.yang@lge.com'"
    query_static_analysis_report = "SELECT Project,LastCommit,KLOC,Total,Opened,Fixed,FalseAlarm,Improvement,Closed,IssueDensity,Status FROM static_analysis_report"
    query_email = 'select email from static_analysis_email' # email list
    # query_coverity_time_table = "static_analysis_coverity_time"


    query_content = '''SELECT A.*
    FROM
        static_analysis_report A,
        ( SELECT Project, MAX(LastCommit) AS LastDate FROM static_analysis_report GROUP BY Project ) B
    WHERE
        B.LastDate  > SUBDATE(SYSDATE(), 6)
        AND A.Project = B.Project
        AND A.LastCommit = B.LastDate
    ORDER BY A.Project ASC
    '''

    query__daily_email_content = '''SELECT A.Project, A.LastCommit, A.KLOC , A.Total , A.FalseAlarm, A.Opened, A.Fixed, A.Closed, A.IssueDensity
    FROM
        static_analysis_report A,
        ( SELECT Project, MAX(LastCommit) AS LastDate FROM static_analysis_report GROUP BY Project ) B
    WHERE
        B.LastDate  > SUBDATE(SYSDATE(), 6)
        AND A.Project = B.Project
        AND A.LastCommit = B.LastDate
    ORDER BY A.Project ASC
    '''




    sql = '''SELECT * FROM static_analysis
    WHERE id IN
    (
            SELECT mid FROM
            (SELECT project_name, MAX(id) mid FROM static_analysis GROUP BY project_name ) A
    )
    AND `date`  > SUBDATE(SYSDATE(), 365)
    ORDER BY id DESC
    '''



    # cur.execute(query_email)
    # connect.commit()
    #
    # # fetchall() : 지정 테이블 안의 모든 데이터를 추출
    # datas = cur.fetchall()
    # for data in datas :
    #     print(data)
    # print('*'*100)
    #
    #


    # cur.execute(query_content)
    cur.execute(query__daily_email_content)

    # cur.execute(query_coverity_time_table)
    # connect.commit()

    print(today_dt_str)
    datas = cur.fetchall()
    cnt_id = 0
    cnt_evc = 0
    coverity_ID_info = []
    coverity_evc_info = []
    # available_days = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    # oebuild_lists = ["LED_Home_Residential","webos23@webos4hotel","webOS23@webos4signage","m16p3@lbs4signage"]

    # for idx, data in enumerate(datas,1) :
    #     print(idx, data[0],data[1])




    st.markdown(dt.today())



    # for idx, data in enumerate(datas,1):
    #     print(idx, data[0], data[1],  format(round(data[2]/1000),','),  format(data[3],','), format(data[4],','),  format(data[5],','), format(data[6],','), format(data[7],','), round(data[8],4) if data[8] !=0 else "0.0000")    





    df = pd.DataFrame(datas)
    df.columns = ["Project","LastCommit","KLOC","Total","FalseAlarm","Opened","Fixed","Closed","IssueDensity"]
    df['Report'] = df['Project'].apply(lambda x: f"http://idedqe.lge.com/sar/module_genExcelData.php?project={str(x)}")
    # df.set_index("Project")

    # df['Report'] = np.nan
    # for i in range(len(df)):
    #     proj = df.iloc[i,0]
    #     url = f"<a href=http://idedqe.lge.com/sar/module_genExcelData.php?project={proj}>Click</a>"
    #     print(url)
        # df.iloc[i,['Report']] = url
        
    check_agree = st.checkbox('[정적분석_이메일] 정적분석 현황 리스트 보기 ')
    if check_agree :
        st.write("이메일 정적분석 현황 리스트 :100:")
        st.dataframe(df,
                column_config={
                    "Report" : st.column_config.LinkColumn(
                        label = "Report",
                        width ="None",
                        help="If you click the link, go to the Report",
                        display_text="Click"
                    )
                },
                hide_index=True,             
                )

    df_download = df.iloc[:,0:9]
    st.download_button(
        label='정적분석 진행 현황 -> CSV로 다운로드',
        data=df_download.to_csv(index=False),
        file_name=f'cov_defects_email_{today_dt_str}.csv',
        mime='text/csv'
    )



    # df['Report'] = webbrowser.open_new_tab(url)
        

    # print(df.describe())

    # button = st.button("정적분석 진행 현황")
    # if button :
    #     st.write(':blue[버튼]이 눌렀습니다. :sparkles:')
    #     st.dataframe(df,
    #              column_config={
    #                  "Report" : st.column_config.LinkColumn(
    #                      label = "Report",
    #                      width ="None",
    #                      help="If you click the link, go to the Report",
    #                      display_text="Click"
    #                  )
    #              },
    #              hide_index=True,             
    #              )








    def load_json(json_file):        
        defect_columns = ['Owner','CID','Checker','Impact','File','Function']
        try :
            with open(json_file, 'r') as f_read :
                json_f = json.load(f_read)
                
                cnt_project = 0
                if len(json_f) == 0:
                    print(f"[{json_file}] json contents length : {len(json_f)}") 
                    return
                
                
                for projects, defects in json_f.items():
                    if projects == None or defects == None : break
                    cnt_project += 1                  
                    
                    
                    if defects :
                        print(f"{cnt_project}. Project : {projects} ")
                        print("*"*100)
                        cnt_defect = 0
                        temp_df = pd.DataFrame(columns=defect_columns)
                        all_defect_list = []
                        for items in defects:
                            cnt_defect += 1
                            
                            print(f"{cnt_defect}. Owner: {items[0]} , CID: {str(items[1])} , Checker: {items[2]} , Impact: {items[3]} , File: {items[4]} , Function: {items[5]}")                            
                            defect_data = [items[0] , str(items[1]) , items[2] , items[3] , items[4] ,items[5] ]                            
                            all_defect_list.append(defect_data)
                        
                        st.subheader(f":sparkles: {projects} :sparkles:")
                        st.write(f"Total Defect : {cnt_defect}")
                        temp_df = pd.DataFrame(all_defect_list , columns = defect_columns)
                        # st.dataframe(temp_df , use_container_width=True, hide_index=True)
                        st.table(temp_df)
                        
                        print("*"*100)
                        print()
                # ret_df = pd.DataFrame(all_defect_list , columns = ['Project','Owner','CID','Checker','Impact','File','Function'])
                # return ret_df


        except IOError :
            print(f"IOError...can not read {json_file}")
            
            

    st.title(":sparkles: Choose defects items :sparkles:")
    oebuild_json_file = "D:\\temp\\oebuild.json"
    tvservice_json_file = "D:\\temp\\tvservice.json"


    # 선택박스 버튼(DropBox)
    mbti = st.selectbox(
        '[Defects list] OEBuild or tvService ?' ,
        ('OEBuild' , 'tvService' , 'None'),
        index=2) # Default값 index값 할당 0,1,2
    if mbti == 'OEBuild':
        st.title(":sparkles: OEBuild's Defects Lists :sparkles:")
        load_json(oebuild_json_file)
        # df_oebuild = load_json(oebuild_json_file)
        # st.dataframe(df_oebuild)
    elif mbti == 'tvService':
        st.title(" :sparkles: tvService's Defects Lists :sparkles: ")
        load_json(tvservice_json_file)
        # df_tvservice = load_json(tvservice_json_file)
        # st.dataframe(df_tvservice)
    else:
        st.write('None :grey_exclamation:')
        # st.json(oebuild_json_file)
        
with tab3 :
    st.header('Excel')
    # st.image('https://static.streamlit.io/examples/owl.jpg')
    check_mp_branch = st.checkbox('양산브랜치 빌드 현황')
    if check_mp_branch :
        st.write("Products Branch Lists. :100:")
        excel_file = "D:\\temp\\mp_branch_241211.xlsx"
        df_excel = pd.read_excel(excel_file, index_col=0 , engine='openpyxl' )
        st.dataframe(df_excel)
        # st.dataframe(df_excel,
        #          column_config={
        #              "Report" : st.column_config.LinkColumn(
        #                  label = "Report",
        #                  width ="None",
        #                  help="If you click the link, go to the Report",
        #                  display_text="Click"
        #              )
        #          },
        #          hide_index=True,             
        #          )

    # st.dataframe(df_excel,
    #              column_config={
    #                  "Report" : st.column_config.LinkColumn(
    #                      label = "Report",
    #                      width ="None",
    #                      help="If you click the link, go to the Report",
    #                      display_text="Click"
    #                  )
    #              },
    #              hide_index=True,             
    #              )






sys.exit(0)



for data in datas :
    # data[0],data[1],data[4] # Project , lastcommit , open_count    
    if not "_FPGA_" in data[0] :
        if "EVC_" in data[0] :
            cnt_evc += 1
            coverity_evc_info.append((cnt_evc,data[0]))
        else :
            if not "QE_Test@" in data[0] :
                cnt_id += 1
                coverity_ID_info.append((cnt_id,data[0]))
                


total_cnt = cnt_id + cnt_evc
print(f'total_cnt : {total_cnt}')
print(f'cnt_evc : {cnt_evc}')
print(f'cnt_id : {cnt_id}')
print('*' * 30)
# print(*coverity_evc_info, sep='\n')
for row in coverity_evc_info:
    print(row[0],row[1])

print('*' * 30)
# print(*coverity_ID_info, sep='\n')
for row in coverity_ID_info:
    print(row[0],row[1])

        




