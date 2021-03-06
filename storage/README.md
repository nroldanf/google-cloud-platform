## Cloud Storage

Object storage means you keep this arbitrary bunch of bytes (binary files) and the storage let adress with a unique key.
It's not a file system.

- Organized into bucket (with global unique names)
- Storage objects are inmutable (create new versions)
- Cloud storage always encript objects by default (without paying extra)
- Data in transit is encrypted using HTTPS
- You can restore an object into an older version.
- Can configure lifecycle management policies to control objects.

__Types of Storage Classes__

How to bring data into s3:

- Using gsutil from Cloud SDK
- Drag and Drop on the GCP Console
- But how about Petabytes of data: online storage transfer service and offline transfer appliance (beta), lets you schedule and manage batch transfer from a different vendor or different cloud storage region or an https endpoint.

Works with other GCP services:
- Import and export tables from __Big Query__
- Object sotrage and logs on __App Engine__
- Start up scripts, images and general object storage in __Compute Engine__
- Import and export tables from __Cloud SQL__

![]()

![]()

## __Cloud Big Table__

- Fully managed No SQL big data databse service for terabyte applicaitons.
- Supports high throughtput both for read and write
- Accessed using HBase API
- Native compatibility with big data Hadoop systems
- Data encription at rest and in flight
- Control access with IAM

__Access Patterns__

- API (read and write)
- Streaming (data can be streamed through a variety of popular streaming service e.g. spark streaming)
- Batch Processing (e.g using Hadoop Map Reduce)

## __Cloud Datastore__

Is an horizontally scalable NoSQL DB.

- Designed for backend applications (e.g. app engine or compute engine)
- aUTOMATICALLY handles replication

## __Cloud SQL__

Cloud SQL is a managed RDBMS

- Offers MySQL, PostgreSQL and SQL service AS a fully managed service
- Terabytes storage
- Automatic replication (within multipl zones)
- Scaling vertically and horizontally 

## __Cloud Spanner__

If cloud sql is not horizontal scalability is not enough.

- Strong global consistency
- Managed instances with high availability


![]()
