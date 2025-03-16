from music21 import stream, note, meter, key

# 簡譜數字對應到 D 大調的五線譜音符
num_to_pitch = {
    '1': 'D', '2': 'E', '3': 'F#', '4': 'G', '5': 'A', '6': 'B', '7': 'C#'
}

# 你的完整簡譜（手動轉錄）
jianpu = [
    "5-1", "3-1", "3-1", "2-1", "7-1", "1-2", "1-2",
    "1-1", "4-1", "3-0.5", "4-0.5", "3-1", "4-1", "1-1", "2-2",
    "3-1", "4-1", "5-1", "5-1", "3-1", "5-1", "3-1", "2-1", "1-1", "0-1",
    "1-1", "4-1", "4-1", "4-1", "3-1", "2-2",
    "3-1", "4-1", "5-1", "3-1", "2-1", "3-1", "2-1", "1-1", "0-1",
    "1-1", "4-1", "4-1", "3-1", "1-1", "2-1",
    "2-1", "3-1", "2-1", "7-1", "1-2", "1-1", "0-1"
]

# 建立樂譜
score = stream.Score()
part = stream.Part()

# 設定調號（D大調）和拍號（4/4）
part.append(key.Key('D'))
part.append(meter.TimeSignature('4/4'))

# 轉換簡譜數字為音符
for jianpu_note in jianpu:
    num, duration = jianpu_note.split('-')  # 分離數字與時值
    if num == '0':  # 休止符
        n = note.Rest()
    else:
        pitch = num_to_pitch.get(num, 'D')  # 取得音名
        n = note.Note(pitch)
    n.quarterLength = float(duration)  # 設定時值
    part.append(n)

# 加入樂譜並顯示
score.append(part)
score.show()
