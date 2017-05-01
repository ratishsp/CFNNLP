import sys

reload(sys)
sys.setdefaultencoding('utf8')

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


if __name__ == '__main__':
    raw_file = '/home/ratish/Downloads/decodedwordsegmentationfilesusingdifferentmodels/6000.raw'
    file_1 = '/home/ratish/Downloads/decodedwordsegmentationfilesusingdifferentmodels/6000.human'
    file_2 = '/home/ratish/Downloads/decodedwordsegmentationfilesusingdifferentmodels/6000.zpar'
    file_3 = '/home/ratish/Downloads/decodedwordsegmentationfilesusingdifferentmodels/6000.neualrichpretrain'

    content_raw = read_file(raw_file)
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content_1 = read_file(file_1)

    content_2 = read_file(file_2)

    content_3 = read_file(file_3)

    output = ''
    for index in range(len(content_raw)):
        line_raw = content_raw[index]
        line_1 = content_1[index]
        line_2 = content_2[index]
        line_3 = content_3[index]

        if line_1 == line_2 and line_2 == line_3:
            continue

        line_1_sub = line_1
        line_2_sub = line_2
        line_3_sub = line_3
        output += '#'+str(index)+'#'
        #print(output)
        for line_index in range(len(line_raw.decode('utf-8'))):
            line_raw_sub = line_raw.decode('utf-8')[line_index:]
            raw_character = line_raw_sub.decode('utf-8')[:1]
            output += raw_character
            #print(line_raw_sub)
            human_char = line_1_sub.decode('utf-8')[:1]
            r1_char = line_2_sub.decode('utf-8')[:1]
            r2_char = line_3_sub.decode('utf-8')[:1]
            #print('raw_character '+raw_character+' human_char '+human_char)
            if human_char == r1_char and r1_char == r2_char and r2_char == raw_character:
                #print('equal raw_character ' + r1_char + ' human_char ' + human_char)
                #print('line_1_sub.decode()[:1] '+line_1_sub.decode('utf-8')[:1])
                line_1_sub = line_1_sub.decode('utf-8')[1:]
                line_2_sub = line_2_sub.decode('utf-8')[1:]
                line_3_sub = line_3_sub.decode('utf-8')[1:]
                continue
            elif human_char == r1_char and r1_char == r2_char and r2_char == ' ':
                line_1_sub = line_1_sub.decode('utf-8')[2:]
                line_2_sub = line_2_sub.decode('utf-8')[2:]
                line_3_sub = line_3_sub.decode('utf-8')[2:]
                continue
            output +='#s'
            #print('line_raw_sub.decode()[:1] ' + raw_character)
            line_1_sub = line_1_sub.decode('utf-8')[1:]
            line_2_sub = line_2_sub.decode('utf-8')[1:]
            line_3_sub = line_3_sub.decode('utf-8')[1:]
            if human_char != raw_character:
                output += 'h1'
                line_1_sub = line_1_sub.decode('utf-8')[1:]
                #print('line_1_sub '+line_1_sub)
            if r1_char != raw_character:
                output += 'r1'
                line_2_sub = line_2_sub.decode('utf-8')[1:]
            if r2_char != raw_character:
                #print('line_3_sub.decode' + r2_char)
                #print('line_raw_sub.decode' + raw_character)
                output += 'r2'
                line_3_sub = line_3_sub.decode('utf-8')[1:]
            output += '#'
        output +="\n"

    print(output)
    #output = output.encode('utf-8')
    outfile = open('/home/ratish/Downloads/decodedwordsegmentationfilesusingdifferentmodels/6000.diff','w')
    outfile.write(output)
    outfile.close()

