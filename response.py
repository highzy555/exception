from random import choice, randint
leprosy_word = [

	"**ควยไรเย็ดแม่**",

	"**หีมึงน่าเย็ดดีจัง**",

	"**ไม่ได้ตึงหรอกไอโง**่",

	"**กูเห็นแม่มึงขายหีอยู่สลัมจริงไหม**",

	"**อย่าเอ๋อไอสัส**",

	"**ทะรุหีเเม่มาเกิด**",

	"**โง่**",

	"**สมเพช**",

	"**ควาย**",

	"**ควย**",

	"**ภาษาไทยวันละคำรู้ปะภาษาไทยเป็นไงไอพม่า**",

	"**แม่มึงอะ**",

	"**ไอควายicหน้าตาดีocหน้าส้นตีนหมาไม่แดก**",

	"**ไม่อยากคุยกับพวกสลัม**",

	"**พ่อมึงตาย**",
	"**นรกส่งมาร่านหรอ**",
	"**ไอจนสภาพมึงยังไม่มีคอมเล่นเลยว๊ายๆๆลูกอีเหี้ยเด็กเบเบ๋อ**",
	"**คนบางคนแถวๆนี้ ก็เหมือนฝุ่น PM2.5 ดูไร้ค่าแถมเป็นพิษ**",
	"**ละเป็นเหี้ยไรอ่ะไอ้เขมรอย่าหลอนยาให้มากไอ้ควายกลับไปกินหมาที่บ้านเกิดมึงนะไอควาย**",
	"**เขาไม่รักอะดิถึงมาคุยกับกูว้ายๆๆๆ**",
	"**มีปัญญาแค่นี้อ่อ**"

]



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return '** # __อย่าเอ๋อ__ **'
    elif 'ควย' in lowered:
        return '**ควยไรละไอสัส**'
    elif 'ชื่ออะไร' in lowered:
        return '** # __ไม่ต้องเสือก!__ **'
    elif 'บาย' in lowered:
        return '**เออไปไกลๆตีน**'
    elif 'กะจอก' in lowered:
        return f'**มึงอะกะจอก เก็บกดหรอไอสัส**'
    elif 'พ่อมึงตาย' in lowered:
        return "** # พ่อมึงอะตายไอสัส **"
    elif 'แม่มึงตาย' in lowered:
        return "** # แม่มึงอะตายไอสัส **"
    elif 'ไร' in lowered:
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
    elif 'เก่งๆ' in lowered:
        return "**เออกูรู้ว่ากูเก่ง**"
    elif 'เล็ก' in lowered:
        return "**ควยกูเล็ก แต่ใหญ่กว่าของมึงนะ**"
    elif 'หรอ' in lowered:
        return "**เออดิ**"
    elif 'หรอวะ' in lowered:
        return "**ช่ายยยยยยย**"
    elif 'สมเพช' in lowered:
        return "**สมเพชพ่อมึงหรอ**"
    elif 'ควยดำ' in lowered:
        return "**ของมึงอะหรอ**"
    elif 'มึง' in lowered:
        return "**ว่า**"
    elif 'กูเห็นแม่มึงขายหีอยู่สลัมจริงไหม' in lowered:
        return "**แม่มึงรึป่าวไอเอ๋อ**"
    elif 'ไม่ใช่' in lowered:
        return "**อ่า**"
    elif 'มึงอะ' in lowered:
        return "**มึงนั่นแหละไอสัส**"
    elif 'ดีครับ' in lowered or 'ดีคับ' in lowered:
        return "**ไปดีกับพ่อมึงนะไอสัส**"
    elif 'ควยไร' in lowered:
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
        return "**เดี๋ยวตายไปมึงก็ได้เป็น**
    else:
        return choice(leprosy_word)
        
        