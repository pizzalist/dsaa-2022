

def is_validate_dom(dom_text : str) -> bool:
    """ dom 문서인 str 타입의 데이터를 받은 후 해당 데이터가 올바른 dom 문서인지 아닌지 확인 하는 코드 
        반드시 stack 또는 queue 를 사용하여 구현할 것
    Args:
        dom_text (str) : dom 문서

    Returns:
        is_valudate_dom (bool) : 해당 문서가 올바른 dom인지 확인하는 코드
    
    """
    # dom_text 의 문장을 나눈다.
    text_line = dom_text.strip().split("\n") #['<data>', '            <items>', '                <item name="item1">item1abc</item>', '                <item name="item2">item2abc</item>', '            </items>', '        </data>']
    text_line2 = []
    
    for i in text_line:
        i = i.strip()
        if i.count('<') == 1 :
        # if i.startswith('<') and i.endswith('>'):
            text_line2.append(i)
        
        elif i.count('<') >= 2:
            print("2개 이상 :",i)
            a = i.replace('>','>#')
            b = a.replace('</','#</')
            c = b.split('#')
            d = list(filter(None, c))  # list 내의 공백 제거
            print("d :",d)
            if ' ' in d[0]:
                first_0 = d[0].split()
                first = first_0[0].replace('<','')
            else:
                first_0 = d[0].replace('<','')
                first = first_0.replace('>','')
            last = d[-1].replace('</','')
            print("ff : " ,first)
            print('last :',last)
            if first == last.replace('>','') and '>' in last:
                pass
            else: 
                text_line2.append(i)
        else:
            text_line2.append(i)
            
    stack = []
    #print(text_line[1].split('<'))
    # '<'포함된 값들 stack에 push
    for i in text_line2:
        # one_part = i.strip().split
        if '<' in i and '</' not in i :
            stack.append(i)
            
        # </같은 값 나오면 pop
        elif '</' in i :
            if i.replace('</','<') in stack:
                stack.pop(-1)
            else: 
                stack.append(i)
                
        
                

    
    # Stack 이 비면 True
    if len(dom_text.strip()) == 0:
        return False
    else: 
        if stack == []:
            print(True)
            return True
        else:
            print(False)
            return False
    
    # if len(stack) == 0:
    #     print(True)
    #     return True
    # else:
    #     print(False)
    #     return False
    



dom_text = '<p id="demo"></p>'
is_validate_dom(dom_text)
    
     
