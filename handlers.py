import telebot
import requests
from config import TASK_REPORT, STORAGE_REPORT, VM_NOTRELIC, VM_RELIC

def get_task_report():
    response = requests.get("TASK_REPORT")
    if response.ok:
        return response.json()
    else:
        return None
    
def get_storage_report():
    response = requests.get("STORAGE_REPORT")
    if response.ok:
        return response.json()
    else :
        return None

def get_vm_relic():
    response = requests.get("VM_RELIC")
    if response.ok:
        return response.json()
    else :
        return None

def get_vm_notrelic():
    response = requests.get("VM_NOTRELIC")
    if response.ok:
        return response.json()
    else :
        return None
    
def initiate_vm_selection(message):
    bot.reply_to(message, "Apakah itu relic?:\n1. ya \n2. tidak \n")
    bot.register_next_step_handler(message, process_vm_type)
    
def process_vm_type(message):
    vm_type = message.text.strip().lower
    
    if vm_type == "ya":
        vm_list = get_vm_relic()
        respond_to_user(message, vm_list)
    elif vm_type == "tidak":
        vm_list = get_vm_notrelic()
        respond_to_user(message, vm_list)
    else:
        bot.reply_to(message,"Input tidak valid.")
    
def respond_to_user(message, vm_list):
    if vm_list:
        vm_names = "\n".join(vm['name'] for vm in vm_list)
        bot.reply_to(message, f"Daftar VM:\n{vm_names}")
    else:
        bot.reply_to(message, "Gagal mendapatkan daftar VM.")
        
@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Hello, Rubrik Bot Here!\n" +
        "To get task report press /taskreport.\n" +
        "To get storage report press /storagereport.\n" +
        "To get all VM press /getvm."
    )
    
@bot.message_handler(commands=["getvm"])
def get_vm_command(message):
    initiate_vm_selection(message)

@bot.message_handler(commands=['taskreport'])
def handle_report_task(message):
    report = get_task_report()
    if report:
        formatted_report = format_report(report)
        bot.reply_to(message, f"Laporan Task:\n{formatted_report}")
    else:
        bot.reply_to(message, "Gagal mendapatkan laporan task.")

@bot.message_handler(commands=['report_storage'])
def handle_report_storage(message):
    report = get_storage_report()
    if report:
        formatted_report = format_report(report)
        bot.reply_to(message, f"Laporan Storage:\n{formatted_report}")
    else:
        bot.reply_to(message, "Gagal mendapatkan laporan storage.")

def format_report(report):
    if not report:
        return "Tidak ada data."

def handle_report_task(message):
    report = get_report_task()
    if report:
        formatted_report = format_report(report)
        bot.reply_to(message, f"Laporan Task:\n{formatted_report}")
    else:
        bot.reply_to(message, "Gagal mendapatkan laporan task.")

@bot.message_handler(commands=['report_storage'])
def handle_report_storage(message):
    report = get_report_storage()
    if report:
        formatted_report = format_report(report)
        bot.reply_to(message, f"Laporan Storage:\n{formatted_report}")
    else:
        bot.reply_to(message, "Gagal mendapatkan laporan storage.")

def format_report(report):
    if not report:
        return "Tidak ada data."
    
    formatted_items = []
    
    for item in report.get('objectCounts', []):
        active = item.get('active', "N/A")
        canceled = item.get('canceled', "N/A")
        failure = item.get('failure', "N/A")
        scheduled = item.get('scheduled', "N/A")
        success = item.get('success', "N/A")
        total = item.get('total', "N/A")
        formatted_items.append(f"active: {active}, Canceled: {canceled}, Failure: {failure}, Scheduled: {scheduled}, Success: {success}, Total: {total}")

    return "\n".join(formatted_items) 

if __name__ == '__main__':
    print("Bot sedang berjalan...")
    bot.polling() 