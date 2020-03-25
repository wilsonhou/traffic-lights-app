# Will write syllabus dot points into a json file
import json


def main():

    # list out addresses of all subject syllabuses to convert
    SUBJECT_LIST = ['chemistry-stage6-syllabus-pdf']
    MODULE_DELIM = '&&&'
    TOPIC_DELIM = '???'
    DP_DELIM = '***'

    # for now, just write syllabus to JSON
    for subject in SUBJECT_LIST:
        ''' REFACTOR THIS FOR DIFFERENT SYLLABUSES! '''
        syllabus_dict = {'modules': []}

        # for each syllabus read a text file then write it as json
        with open(f"../syllabus/{subject}.txt") as infile:
            # split file by module and create module dict in syllabus dict
            module_blocks = [module_block for idx, module_block in enumerate(
                infile.read().split(MODULE_DELIM)) if idx % 2 != 0]

            # construct module dict to add to syllabus dict
            for module in module_blocks:
                new_module = {'name': '', 'topics': []}
                # ! how else can we do this... refactor into a function?
                # TODO: REFACTOR THIS!!!
                new_module['name'] = module.split('\n')[1]

                # for each module, split by topic and make topic dicts to add onto module dicts
                topic_blocks = [topic_block for idx, topic_block in enumerate(
                    module.split(TOPIC_DELIM)) if idx % 2 != 0]

                # construct topic dict to add to module dict
                for topic in topic_blocks:
                    new_topic = {'name': '', 'content': 'Test'}
                    new_topic['name'] = topic.split('\n')[1]

                    new_module['topics'].append(new_topic)

                # add new module dict to the syllabus dict
                syllabus_dict['modules'].append(new_module)

        # write end file as json
        with open(f"../end-data/{subject}.json", "w") as outfile:
            outfile.write(json.dumps(syllabus_dict))
            # outfile.write("\n".join(topic_blocks))


if __name__ == '__main__':
    main()
