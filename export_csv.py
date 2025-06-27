import csv

def export_to_csv(data, filename='captured_data.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Details'])  # Header row

        for item in data:
            writer.writerow([item['type'], item['details']])  # Write each data item

def prepare_data_for_export(metro_ethernet_frames, sdh_frames, mpls_labels):
    data = []

    for frame in metro_ethernet_frames:
        data.append({'type': 'Metro Ethernet', 'details': frame.show_frame()})

    for frame in sdh_frames:
        data.append({'type': 'SDH/SONET', 'details': frame.show_frame()})

    for label in mpls_labels:
        data.append({'type': 'MPLS Label', 'details': label.show_label()})

    return data