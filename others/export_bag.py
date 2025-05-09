import csv
import rosbag2_py

def export_bag_to_csv(bag_path, output_csv):
    storage_options = rosbag2_py.StorageOptions(uri=bag_path, storage_id='mcap')
    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format='cdr',
        output_serialization_format='cdr'
    )

    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)

    with open(output_csv, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['timestamp', 'joint_name', 'effort'])

        while reader.has_next():
            topic, data, timestamp = reader.read_next()
            if topic == '/joint_states':
                # Decodifica el mensaje
                from sensor_msgs.msg import JointState
                import rclpy.serialization
                joint_state = rclpy.serialization.deserialize_message(data, JointState)

                for name, effort in zip(joint_state.name, joint_state.effort):
                    csv_writer.writerow([timestamp, name, effort])

def export_wheel_positions_to_csv(bag_path, output_csv):
    storage_options = rosbag2_py.StorageOptions(uri=bag_path, storage_id='mcap')
    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format='cdr',
        output_serialization_format='cdr'
    )

    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)

    with open(output_csv, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['timestamp', 'joint_name', 'position'])

        while reader.has_next():
            topic, data, timestamp = reader.read_next()
            if topic == '/joint_states':
                from sensor_msgs.msg import JointState
                import rclpy.serialization
                joint_state = rclpy.serialization.deserialize_message(data, JointState)

                for name, position in zip(joint_state.name, joint_state.position):
                    csv_writer.writerow([timestamp, name, position])

if __name__ == '__main__':
    bag_path = 'rosbag'
    
    output_csv = 'joint_states.csv'
    export_bag_to_csv(bag_path, output_csv)

    output_csv = 'wheel_positions.csv'
    export_wheel_positions_to_csv(bag_path, output_csv)

    print(f'Datos exportados a {output_csv}')