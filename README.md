![Logo](./images/taligent.jpg)

# Ejercicio IAC - SSR Level

Se disponibilizo un usuario IAM con acceso a los siguientes servicios en la plataforma de Amazon Web Services:
- S3
- Data Migration Service
- VPC
- Glue
- Athena
- Cloud Formation

## Requerimientos

Se requiere construir una arquitectura que satisfaga el siguiente diagrama

<img src="images/arquitectura.png" width="750" height="600"/>

- Se disponibilizo un set de datos no catalogados en esta carpeta: s3://challenge-aws-iac/
- Dichos datos deben ser migrados en la siguiente carpeta: s3://challenge-aws-iac-target-dms
- Los datos destino deben ser limpiados y catalogados en Glue
- Considerar la lógica de negocio y los datos de la bajada para mostrar información significativa. Pueden generar nuevas vistas de Athena de ser necesario (por lo general estos indicadores se desarrollan en la misma herramienta de BI pero vamos a focalizarnos en AWS y uso de SQL)
- Los datos transformados deben poder ser accesibles en formato tabla

## Notas
El template entregado debe ser en un formato valido de Cloud Formation (JSON o YAML)

Excepto el bucket con la data inicial, todo lo necesario para completar el ejercicio debe ser creado en el template de CloudFormation

La instancia de DMS que se va a utilizar es la t3.micro que ya va a disponibilizada en la cuenta de AWS pero en el entregable igualmente debe estar incluido toda la configuracion en el codigo para levantar la instancia desde cero

Etiquetar todos los recursos como:

Key; Interno  
Value: Ejercicio-IaC

<br>

## Forma de entrega

Una vez finalizado el ejercicio, se debe hacer un pull request al repositorio y dentro debe estar el template de CloudFormation
