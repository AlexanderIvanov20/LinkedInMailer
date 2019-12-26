from linkedin_api import *


PUBLIC_IDS = set()


class LinkedinHandler:
    # ? Initiate object of LinkedIn class
    def __init__(self, username: str, password: str) -> None:
        with open('users.txt', 'w', encoding='utf-8') as file:
            file.write('Test\n')
        self.linkedin = Linkedin(username=username,
                                 password=password)

    # ? Get and reply on invitational
    def invitationals(self) -> None:
        invitationals = self.linkedin.get_invitations()
        print('Point on invites: ', invitationals[0])

        for invite in invitationals:
            self.linkedin.reply_invitation(invitation_entity_urn=invite['entityUrn'],
                                           invitation_shared_secret=invite['sharedSecret'])

    # ? Send messages
    def send_message_by_urn(self, response_text: str) -> None:
        # ? Get conversation and send message to the user
        print('Point on conversation: ', PUBLIC_IDS)

        for profile_urn_id in PUBLIC_IDS:
            conversation = self.linkedin.get_conversation_details(
                profile_urn_id)
            conversation_id = conversation['id']

            error = self.linkedin.send_message(conversation_urn_id=conversation_id,
                                               message_body=response_text)
            # ! If error is arises
            if error:
                print(True)

    # ? Search by people
    def search_users(self, keyword_for_search: str, region_for_search: str, limit: int, response_text: str) -> None:
        results = self.linkedin.search_people(keywords=f'{keyword_for_search}',
                                              regions=[f'{region_for_search}'],
                                              limit=limit)
        print(results)

        with open('users.txt', 'r', encoding='utf-8') as file:
            file_content = file.readlines()
        file_content_list = [item.replace('\n', '') for item in file_content]

        # ? Get urn ids by search
        with open('users.txt', 'a', encoding='utf-8') as file:
            for user in results:
                if user['urn_id'] not in file_content_list:
                    file.write(f"{user['urn_id']}\n")
                PUBLIC_IDS.add(user['urn_id'])

        self.send_message_by_urn(response_text)

    # ? Send message to current user
    def send_message_to_current(self, response_text):
        # ? Get conversation and send message to the user
        profile = self.linkedin.get_profile('kirill-asieiev-6344a619a')
        profile_urn_id = profile['profile_id']
        print(profile)

        conversation = self.linkedin.get_conversation_details(
            profile_urn_id)
        conversation_id = conversation['id']

        error = self.linkedin.send_message(conversation_urn_id=conversation_id,
                                           message_body=response_text)
        # ! If error is arises
        if error:
            print(True)


linked = LinkedinHandler('alexander.ivanov.289@gmail.com', 'Domestos03')
# linked = LinkedinHandler('mup.folesta@gmail.com', 'Nikita777')
linked.send_message_to_current(
    'Сообщение отправлено 12/19/2019')
