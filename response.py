from random import choice, randint
highzy1 = ["**ควยไรละไอสัส**","**ควยไรไอเอ๋อ**","**ควยไรไอโง**่","**ควยไรละไอควาย**","**เหี้ยไรมึงไอเอ๋อ**","**แล้วเป็นควยไรอะ**","**ควยดำๆของมึงอะไออ้วน**","ควยไร","เหี้ยไรมึงไอ้อ้วน"]
highzy2 = ["**รังสิตไงไอโง่**","**รัชดาไงไอควาย**","**พระราม9ไงมึงไม่รู้จักหรอ555555**","**อ่อนนุชไงไอสัส**","**สยามไงไอเด็กกะแบ๊**","**ที่เขมรไงแม่มึงไปขายบ่อย5555**","**แถวสวนลุมพินี**"]
submit1 = ["ไออ๋อง","ไอเอ๋อ","ไอควาย","ไอกระจอก","ไอโง่","ไอกาก","ไออ้วน","ไอดำ","ไอเหี้ยอ้วนตัวย้วย","ไม่เต็ม","ใบโพล่า","เขมร"]
submit2 = ["**ควยไรอะ**","**แล้วเป็นเหี้ยไรมากป่ะไอสัส**","**ไอจน**","**ไอบ้านนอกไม่มีจะกิน**","**ขอทานว้ายๆๆ**","**บ้านมึงกูนึกว่ารังหนู**","**เสร่อ**","**คนอีสานกูไม่คุยด้วย**","**เมียมึงอะโดนกูเย็ดแล้ว55555**"]
hello1 = ["สวัสดีครับ","สวัสดีค่ะ","ดีครับ","ดีคับ","ดีค่ะ","ดีคร่ะ","สวัสดีคับ","hi","Hi","hI","Hello","hello","heloo","Heloo","หวัดดี","หวัดดีครับ","หวัดดีคับ"]
hello2 = ["**ดีครับไอสัส**",'**ดีคับไอสัส**',"**ดีครับไอเด็กกระแบ๊**","**ดีครับไอควาย**","**ไปหวัดดีพ่อมึงนู่นไออ้วน**","**สวัสดีค่ะ**","**ไปหวัดดีแม่มึงเถอะ**","**ดีจ้า**","**สวัสดีจ้า**"]
submit =["**แม่มึงอะนิสัยดีจะตายแต่ลูกแม่งสมองหมาปัญญาควาย**","**ไอชั้นต่ำ**","**พ่อมึงป่าวเมื่อวานกูเห็นพ่อมึงขับรถชนเสาไฟฟ้าตาย**","**แม่มึงขายหีแทบตายแต่ลูกมานั่งเล่นโทรศัพท์ทั้งวัน**","**มานั่งโชว์พาวลาวโลกหาแม่มึงอะไอเด็กเสี่ยว**","**เด๋วกูเตะเด๋วกูต่อย**","**ปัญญาอ่อน**","**โดนฝนอาจเป็นหวัดโดนซัดอาจเป็นมึง**","**ควยไรลูกอีโสกัง**","**พวกมึงก็เเค่เกมที่กูสร้างขึ้นมาหมดประโยชกูก็โยนทิ้งเหมือนพวกไร้ค่า**","**กระแดะหาพ่อมึงหรอ**","**ไอหน้าตาอัปลักษณ์หน้าหีอัปปรีย์**","**ถ้ามันหันมาด่ากูกลับเท่ากับว่ามันมาเป็นหมากรุกในกระดานกูแล้ว**","**ไปบอกพ่อมึงนะไอติ๋ม**","**มาขายขำหรอถามจริง**","**คำพูดคำจาไม่มีมาให้กูด่าฟรีไปวันๆ**","**ไอเหี้ยนี่ปัญญาอ่อน**","**ส้นตีนกูก็เหมือนช้อปปี้ ที่พร้อมส่งฟรีถึงหน้ามึง**","**ที่แม่มึงรวยเพราะแม่มึงคลานมาอมควยกู**","**สภาพเบ้าหน้ามึงเหมือนวัว**","**ตกลงมาจากชั้น10โดนรถสิบล้อทับไปทับมาทับไปทับมา แล้วกลิ้ง ครึก ครึก ครึก ครึก ไปสลบหน้าแนบคาตีนกู**","**ลูกกระหรี่อย่าหลอนไอควยมึงดูอนิเมะมากไปหรออัญเชิญผู้กล้าต่างโลกไรงี้ปะว่างๆนะมึงตื่นมาดูความจริงมั่งไอเด็กนรก**","**ก่อนเข้าดิสมึงแดกหญ้ามาหรอ**","**กูใช้โทรจันแฮกกล้องมึงอยู่นั่นบ้านหรอกูนึกว่ารังหนู**","**ไอเหี้ยนี่โง่เป็ยควายเลยนะครับปล่อยให้กูด่าฟรีสมเพชจัดไร้สมอง**"]


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return '** # __อย่าเอ๋อ__ **'
    elif lowered == 'ควย':
        return choice(highzy1)
    elif lowered in hello1:
        return choice(hello2)
    elif 'ชื่ออะไร' in lowered:
        return '** # __ไม่ต้องเสือก!__ **'
    elif lowered in submit1:
        return choice(submit2)
    elif 'บาย' in lowered:
        return '**เออไปไกลๆตีน**'
    elif 'กะจอก' in lowered:
        return f'**มึงอะกะจอก เก็บกดหรอไอสัส**'
    elif 'พ่อมึงตาย' in lowered:
        return "** # พ่อมึงอะตายไอสัส **"
    elif 'แม่มึงตาย' in lowered:
        return "** # แม่มึงอะตายไอสัส **"
    elif 'ควยไร' in lowered:
        return "**ควยไรอีดอก**"
    elif 'โง่' in lowered:
        return "**ครับไอสัส**"
    elif 'ควาย' in lowered:
        return "**มึงด่าพ่อมึงทำไม**"
    elif 'เงี่ยน' in lowered:
        return "**มาอมควยกูมา**"
    elif 'เสือก' in lowered:
        return "**เสือกเหี้ยไร อย่าเอ๋อดิ**"
    elif 'กระจอก' in lowered:
        return "**กระจอกพ่อกระจอกแม่มึงอะอีสัส**"
    elif lowered == 'เก่ง' or lowered == 'เก่งๆ':
        return "**เออกูรู้ว่ากูเก่ง**"
    elif lowered == 'ควยเล็ก':
        return "**ควยกูเล็ก แต่ใหญ่กว่าของมึงนะ**"
    elif lowered == 'หรอ':
        return "**เออดิ**"
    elif 'หรอวะ' in lowered:
        return "**ช่ายยยยยยย**"
    elif 'สมเพช' in lowered:
        return "**สมเพชพ่อมึงหรอ**"
    elif lowered == 'ควยดำ':
        return "**ของมึงอะหรอ**"
    elif lowered == 'มึง':
        return "**ว่า**"
    elif 'กูเห็นแม่มึงขายหีอยู่สลัมจริงไหม' in lowered:
        return "**แม่มึงรึป่าวไอเอ๋อ**"
    elif lowered == 'ไม่ใช่':
        return "**อ่า**"
    elif lowered == "มึงอะ":
        return "**มึงนั่นแหละไอสัส**"
    elif 'ดีครับ' in lowered or 'ดีคับ' in lowered:
        return "**ไปดีกับพ่อมึงนะไอสัส**"
    elif 'ไร' in lowered:
        return "**ควยไรอีดอก**"
    elif '555' in lowered or '5' in lowered:
        return "**กูตลกกับมึงมั้ย**"
    elif 'สลัม' in lowered or 'สะลัม' in lowered:
        return "**พ่อมึงไงที่เป็นสลัม**"
    elif 'เสร่อ' in lowered or 'ยุ่ง' in lowered:
        return "**ยอมรับความจริงไม่ได้หรอไอควาย😆**"
    elif 'อีสาน' in lowered or 'คนอีสาน' in lowered:
        return "**อีสานแล้วมันหนักหัวพ่อมึงหรอ**"
    elif 'kuy' in lowered or 'kay' in lowered:
        return "**เขียนภาษาไทยไม่เป็นหรอไอสัส**"
    elif 'โง่' in lowered or 'ไม่มีสมอง' in lowered:
        return "**แล้วมึงเสือกควยไรอะ**"
    elif 'เก' in lowered or 'เกย์' in lowered:
        return "**เกควยไร อยากโดนเย็ดหรอไอสัส**"
    elif 'ไม่ได้อยากรู้' in lowered or 'บอกทำไม' in lowered:
        return "**กูอยากบอก มีควยไรป่ะ**"
    elif 'มี' in lowered or 'yes' in lowered:
        return "**เออ**"
    elif 'หลอน' in lowered or 'ไม่เต็ม' in lowered:
        return "**สมองดีกว่ามึงละกัน**"
    elif 'บอทกาก' in lowered or 'ควาย' in lowered:
        return "**เก่งกว่ามึงอะ**"
    elif 'ใช่' in lowered or 'ช่าย' in lowered:
        return "**สมน้ำหน้า55555555**"
    elif 'อ้วน' in lowered or 'ตัวย้วย' in lowered:
        return "**เข้าพ่อมึงเต็มๆเลย55555555**"
    elif 'ดำ' in lowered or 'black' in lowered:
        return "**ถ้ากูดำ มึงน่าจะเป็นขี้เถ้านะไอสลัม**"
    elif 'อ่อนแอก็แพ้ไป' in lowered:
        return "**อ่อนพ่ออ่อนแม่มึงอะไอลูกกระหรี่50**"
    elif 'กะหรี่' in lowered or 'กระหรี่' in lowered:
        return "**แม่มึงอะหรอที่ขายหีอะ**"
    elif 'สภาพ' in lowered or 'สะพาบ' in lowered:
        return "**สภาพเมียมึงที่โดนกูเย็ดสดแตกในไง**"
    elif 'เรื้อน' in lowered:
        return "**ถึงกูจะเรื้อน แต่กูมีมารยาทกว่ามึงนะ**"
    elif 'สวะ' in lowered or 'สะวะ' in lowered:
        return "**มึงไงควายมีเขางอกละนั่น**"
    elif 'เตี้ย' in lowered:
        return "**ขาดความอบอุ่นหรอ ถึงต้องมาบูลลี่คนอื่นอะ**"
    elif 'เปรต' in lowered:
        return "**เดี๋ยวตายไปมึงก็ได้เป็น**"
    elif lowered == 'แร็บ':
        return "**แร็บเอกโจ้ๆ**"
    elif lowered == 'เอ๋อ':
        return "**อย่าอ๋องไอสัส**"
    elif lowered == 'เท่ดิ':
        return "**เท่ดิ ก็กูมันหล่อเป็นที่ต้องการของสาวๆ**"
    elif 'มั่นหน้า' in lowered:
        return "**แล้วเสือกควยไรอะ**"
    elif lowered == 'พายมึงต้อ':
        return "**พ่อมึงอะตาย ไอบ้านนอก**"
    elif lowered == 'บ้านนอก':
        return "**บ้านนอกก็บ้านมึงไง ลืมกำพืดตัวเองหรอไอสลัม**"
    elif lowered == 'ตลกก็ได้':
        return "**555555555555**"
    elif lowered == 'เค' or lowered == 'เคร':
        return "**เคควยไรไอบ้านอก**"
    elif 'Bruh' == lowered or 'bruh' == lowered:
        return "**Bruh!!!**"
    elif 'เคครับ' in lowered:
        return "**ครับไอเหี้ยอ้วน**"
    elif 'Hi' in lowered:
        return "**สวัสดีครับ**"
    elif 'ขำดิ' in lowered:
        return "**ขำควยไรไอสัส**"
    elif lowered == 'เรียกกูว่าพ่อ':
        return "**มีพ่อแบบมึงกูยอมไม่มีดีกว่า**"
    elif 'แร็บ' in lowered:
        return "**แร็บเอกโจ้ๆ**"
    elif 'บอทเอ๋อๆ' in lowered:
        return "**เอ๋อเหี้ยไรมึง**"
    elif 'ค่ะพี่' in lowered:
        return "**ขอดูหีหน่อยดิ**"
    elif lowered == 'ที่ไหน':
        return choice(highzy2)
    elif 'เด็กกระแบ๊' in lowered:
        return "**เด็กควยไร กูลูกคนโตไอโง่**"
    elif 'วันพืช' in lowered or 'ลูฟี่' in lowered:
        return "**โตเป็นควายละ ยังเบียวการ์ตูนอยู่อีกหรอ5665555356**"
    elif lowered == 'เบียว':
        return "**เบียวควยไร ไอเด็กกะแบ๊**"
    elif 'อายาโนะโคจิ' in lowered:
        return "**เบียวควยไรเนี่ย**"
    elif lowered == 'พม่า':
        return "**พม่าก็บ้านเกิดมึงไง😆**"
    elif lowered == 'เขมร':
        return "**มึงไปขายตูดที่เขมรหรอ55555**"
    elif lowered == "ลาว":
        return "**ลาวควยไรไออ๋อง**"
    elif lowered == "เสว":
        return "**เสวเหี้ยไรมึง**"
    elif lowered == "เสียว":
        return "**โดนนิโกเย็ดหรอ55555**"
    elif lowered == "ขยะเปียก":
        return "**ขยะเปียกยังมีค่ากว่าชีวิตมึงเลย**"
    elif lowered == 'หีดำ':
        return "**หีแม่มึงไง ดำจิง**"
    elif lowered == 'ฮับ':
        return "**ฮับพ่อฮับแม่มึงอะไอเอ๋อ**"
    elif lowered == 'งับ':
        return "**งับไรมึง เอ๋อควยไรเนี่ย**"
    else:
        return choice(submit)
        
        