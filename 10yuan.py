import requests
import os
from notify import send


cookie = os.environ.get('MT_COOKIE')

templateNo = os.environ.get('templateNo')  # 购票模板号
phone = os.environ.get('phone')  # 手机号
certificateNum =  os.environ.get('certificateNum')  # 身份证号
chainId = os.environ.get('chainId')  # 票务公司 ID

# 第一步：发送初始请求，获取 token 和 orderId
login_url = 'https://www.kaboss.cn/ticket/outUser/login/user'
login_headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Origin': 'https://ticket.kaboss.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ticket.kaboss.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-gpc': '1'
}
login_payload = {
    'phone': phone,
    'certificateNum': certificateNum,
    'chainId': chainId,
    'templateNo': templateNo
}

# 发送初始 POST 请求
response = requests.post(login_url, headers=login_headers, json=login_payload)

# 检查响应状态码
if response.status_code == 200:
    response_data = response.json()
    
    # 提取 token 和 orderId
    token = response_data['data']['token']
    order_id = response_data['data']['orderInfos'][0]['orderId']
    
    # 第二步：使用 token 和 orderId 发送请求
    template_list_url = 'https://www.kaboss.cn/ticket/outUser/templateList'
    template_list_headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': f'Bearer {token}',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://ticket.kaboss.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://ticket.kaboss.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1'
    }
    template_list_payload = {
        'chainId': chainId,
        'templateNo': templateNo,
        'orderId': order_id  # 使用 orderId
    }

    # 发送带有 token 和 orderId 的 POST 请求
    response = requests.post(template_list_url, headers=template_list_headers, json=template_list_payload)

    # 检查响应状态码
    if response.status_code == 200:
        response_data = response.json()
        template_id = response_data['data'][0]['templateId']

        # 第三步：使用 token 和 templateId 发送请求
        ticket_template_url = 'https://www.kaboss.cn/ticket/outUser/ticketOutside/getOutsideTicketTemplate'
        ticket_template_headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Authorization': f'Bearer {token}',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'DNT': '1',
            'Origin': 'https://ticket.kaboss.cn',
            'Pragma': 'no-cache',
            'Referer': 'https://ticket.kaboss.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-gpc': '1'
        }
        ticket_template_payload = {
            'templateId': template_id
        }

        # 发送带有 token 和 templateId 的 POST 请求
        response = requests.post(ticket_template_url, headers=ticket_template_headers, json=ticket_template_payload)

        # 检查响应状态码
        if response.status_code == 200:
            field = response_data['data'][0]['outsideTemplateField']


            template_list_url = "https://www.kaboss.cn/ticket/outUser/templateList"
            template_list_headers = {
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Authorization": f"Bearer {token}",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "DNT": "1",
                "Origin": "https://ticket.kaboss.cn",
                "Pragma": "no-cache",
                "Referer": "https://ticket.kaboss.cn/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
                "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-gpc": "1"
            }
            template_list_payload = {
                "chainId": chainId,
                "templateNo": templateNo
            }

            template_list_response = requests.post(template_list_url, headers=template_list_headers, json=template_list_payload)
            if template_list_response.status_code == 200:
                template_list_data = template_list_response.json()
                outsideTicketField = template_list_data['data'][0]['outsideTemplateField']

                # Step 3: 使用提取的数据构建 /ticketOutside/create 请求
                create_url = "https://www.kaboss.cn/ticket/outUser/ticketOutside/create"
                create_headers = {
                    "Accept": "*/*",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "Authorization": f"Bearer {token}",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "DNT": "1",
                    "Origin": "https://ticket.kaboss.cn",
                    "Pragma": "no-cache",
                    "Referer": "https://ticket.kaboss.cn/",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
                    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "sec-gpc": "1"
                }
                create_payload = {
                    "chainId": chainId,
                    "orderId": order_id,
                    "outsideTicketField": outsideTicketField,
                    "templateTitle": "京东店铺返费登记",
                    "templateId": template_id,
                    "templateNo": templateNo,
                    "attachments": [],
                    "content": "店铺返费",
                    "title": "京东店铺返费",
                    "field": field,
                    "rebateFreezeRecord": []
                }

                # 发送带有 token 和 orderId 的 POST 请求
                create_response = requests.post(create_url, headers=create_headers, json=create_payload)
                if create_response.status_code == 200:
                    msg = create_response.json()['msg']
                    send('京东返费登记', msg)
                    print(msg)
                else:
                    send('京东返费登记', f"请求失败，状态码：{create_response.status_code}")
                    print("请求失败", create_response.status_code)

        else:
            send('京东返费登记', f"获取票务模板失败，状态码：{response.status_code}")
            print("获取票务模板失败", response.status_code)
    else:
        send('京东返费登记', f"获取票务模板失败，状态码：{response.status_code}")
        print("获取票务模板失败", response.status_code)
else:
    send('京东返费登记', f"初始登录失败，状态码：{response.status_code}")
    print("初始登录失败", response.status_code)
