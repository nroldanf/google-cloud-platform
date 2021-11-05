# Virtual Machines

With Google Compute Engine and Google Virtual Networking.

## Virtual Private Cloud (VPC)

- Each VPC network is contained in a GCP project. You can connect resources to each other, and isolate them from one another. 
- Use firewall rules to restrict access to instances.
- VPC have global scope and can have subnets in any region worldwide
- Can have resources in different zones in the same subnet.

## Compute Engine

- Linux, Windows boot images or bring your own.
- Charge by second.
- Pick memory and CPU from predefined ones or make a custom vm
- Pick and attach GPU if you need them.
- Two kinds of Persistent storage: Standard or SSD. For local SSDK this does not last once the vm terminates.
- Define a start up script if you like (for bootstraping).
- Take snapshots of the disk to keep as backup or migrate vm to somewhere else.
- Huge VM or Autoscaling for resilient scalable applications.
- Load balancing for distributing traffic.

__Differences between EC2 and Compute Engine__

- Faster spin-ups (seconds)
- Preemptible VMS nearly up to 80% savings (AWS Spot Instances)
- Discount Pricing

![AWS Instances vs GCP Virtual Machines](vm_v_instances.png)


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

## __Cloud SQL__


