import "./moduleLayout.css";

function ModuleLayout({

    title,
    description,
    button,
    stats,
    children

}) {

    return (

        <>

            <div className="page-hero">

                <div>

                    <h1>{title}</h1>

                    <p>{description}</p>

                </div>

                <button className="primary-btn">

                    {button}

                </button>

            </div>

            <div className="stats-grid">

                {stats.map((item) => (

                    <div
                        className="card-box"
                        key={item.title}
                    >

                        <h3>{item.title}</h3>

                        <h1>{item.value}</h1>

                    </div>

                ))}

            </div>

            <div className="table-toolbar">

                <input placeholder="🔍 Search..." />

                <button className="primary-btn">

                    Filter

                </button>

            </div>

            {children}

        </>

    );

}

export default ModuleLayout;