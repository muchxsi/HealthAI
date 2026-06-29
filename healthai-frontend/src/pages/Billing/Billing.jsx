import { useEffect, useState } from "react";
import ModuleLayout from "../../components/common/ModuleLayout";
import { getBills } from "../../services/billingService";

function Billing() {

    const [bills, setBills] = useState([]);

    useEffect(() => {

        getBills()
            .then((data) => setBills(data))
            .catch((err) => console.error(err));

    }, []);

    return (

        <ModuleLayout

            title="💰 Billing"

            description="Manage invoices and payments."

            button="+ New Invoice"

            stats={[

                {
                    title: "Invoices",
                    value: bills.length
                },

                {
                    title: "Paid",
                    value: 28
                },

                {
                    title: "Pending",
                    value: 6
                },

                {
                    title: "Revenue",
                    value: "KSh 2.4M"
                }

            ]}

        >

            <div className="recent-patients">

                <table className="patients-table">

                    <thead>

                        <tr>

                            <th>Patient</th>

                            <th>Amount</th>

                            <th>Status</th>

                        </tr>

                    </thead>

                    <tbody>

                        {bills.map((bill, index) => (

                            <tr key={index}>

                                <td>{bill.patient}</td>

                                <td>KSh {bill.amount}</td>

                                <td>{bill.status}</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </ModuleLayout>

    );

}

export default Billing;