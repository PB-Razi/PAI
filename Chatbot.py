class HospitalAppointmentChatbot:
    def __init__(self):
        self.context = {
            'patient': None,
            'appointment': None,
            'doctor': None,
            'department': None,
            'date': None,
            'time': None,
            'address': None,
            'payment_status': None
        }

    def greet(self):
        self.context['patient'] = input("Hello! What's your name?\n")
        print(f"Hello {self.context['patient']}, I'm here to help you schedule a hospital appointment.\n")

    def get_appointment_details(self):
        self.context['department'] = input("What department would you like to visit? (Cardio, Ortho, Neuro, Gync, General)\n")
        self.context['doctor'] = input(f"Who would you like to see in the {self.context['department']} department? (Dr. Jagadeesh MS, Dr. Ravikiran MS, Dr. Jaggu MS, Dr. Sanju MS, Dr. Tanishq MS)\n")
        self.context['date'] = input("What date would you like to come in? (format: MM/DD/YYYY)\n")
        self.context['time'] = input("What time would you like to come in? (09:00, 10:00, 11:00, 12:00)\n")
        self.context['address'] = input("Is this a pickup appointment? If yes, please provide your address.\n")

    def confirm_appointment(self):
        print(f"\nOkay, {self.context['patient']}. Here are the details of your appointment:\n")
        print(f"Department: {self.context['department']}\n")
        print(f"Doctor: {self.context['doctor']}\n")
        print(f"Date: {self.context['date']}\n")
        print(f"Time: {self.context['time']}\n")
        if self.context['address']:
            print(f"Address: {self.context['address']}\n")
        print("Is everything correct? (yes/no)\n")
        confirmation = input()
        if confirmation.lower() == "yes":
            self.context['payment_status'] = "unpaid"
            print(f"Great, {self.context['patient']}! Your appointment with {self.context['doctor']} at {self.context['time']} on {self.context['date']} has been confirmed. Please make sure to arrive at the hospital 10-15 minutes before your appointment time. The consultation fee is $50. Would you like to make the payment now? (yes/no)\n")
            payment_confirmation = input()
            if payment_confirmation.lower() == "yes":
                self.context['payment_status'] = "paid"
                print(f"Thank you, {self.context['patient']}! Your appointment and payment have been confirmed. See you on {self.context['date']}!\n")
            else:
                print(f"No problem, {self.context['patient']}. You can make the payment at the hospital during your appointment. Is there anything else I can assist you with? (yes/no)\n")
        else:
            print("Okay, let's try that again.\n")
            self.get_appointment_details()
            self.confirm_appointment()

    def run(self):
        self.greet()
        self.get_appointment_details()
        self.confirm_appointment()


if __name__ == "__main__":
    appointment_chatbot = HospitalAppointmentChatbot()
    appointment_chatbot.run()
