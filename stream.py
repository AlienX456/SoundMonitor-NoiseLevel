from kafka import KafkaConsumer, KafkaProducer
from Resources.CicloVidaControl import CicloVidaControl
from json import dumps
import os
import logging
import uuid
service_identifier = uuid.uuid4().__str__()
try:

    consumer = KafkaConsumer(os.environ['DATA_UPLOAD_EVENT'],
                             group_id=os.environ['GROUP_ID'],
                             bootstrap_servers=[os.environ['KAFKA_BOOTSTRAP_SERVER_ONE']],
                             auto_offset_reset='earliest',
                             enable_auto_commit='true')
    producer = KafkaProducer(bootstrap_servers=[os.environ['KAFKA_BOOTSTRAP_SERVER_ONE']],
                             value_serializer=lambda x: dumps(x).encode(os.environ['ENCODE_FORMAT']))

    cicloVidaControl = CicloVidaControl()




    for message in consumer:
        fileName = message.value.decode(os.environ['ENCODE_FORMAT'])
        logging.info("New Audio arrived ID %s to consumer %s", fileName, service_identifier)
        try:
            Leq = cicloVidaControl.processAudio(fileName)
            dataToSend = {'device_info': {'audio_uuid': fileName}, "noise_level": Leq}
            producer.send(os.environ['PROCESS_RESULT_EVENT'], value=dataToSend)
            logging.info("%s Jobs Finished", fileName)
        except Exception as e:
            logging.error('Error: "%s" on Consumer "%s" for file "%s"', str(e), service_identifier, fileName)

except Exception as e:
    logging.error('There was an error while Connecting: %s', str(e))